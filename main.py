# !/usr/bin/env python
# -*- coding: utf-8 -*-

from imap_tools import MailBox, AND, A
import imap_tools
import telebot
from os import path


def read_config():
    basedir = path.abspath(path.dirname(__file__))
    with open(path.join(basedir, '.env'), 'r') as f:
        config = dict(
            tuple(line.replace('\n', '').split('='))
            for line in f.readlines() if not line.startswith('#')
        )
    f.close()
    return config


def tg_bot(img):
    config = read_config()
    user_id = config['USER_ID']
    bot_token = config['BOT_TOKEN']
    bot = telebot.TeleBot(bot_token)
    bot.send_photo(user_id, img)
    bot.stop_bot()


def get_mail():
    config = read_config()
    server = config['IMAP']
    login = config['MAIL']
    pwd = config['PASSWORD']
    file_suffix = ('jpeg', 'jpg', 'png')
    try:
        mailbox = MailBox(server).login(login, pwd)
        for msg in mailbox.fetch(A(seen=False)):
            for att in msg.attachments:
                ext = att.filename.lower()
                if ext.endswith(file_suffix):
                    img = att.payload
                    tg_bot(img)
        flags = imap_tools.MailMessageFlags.SEEN
        mailbox.flag(mailbox.uids(AND(seen=True)), flags, True)
        mailbox.logout()
        return True
    except Exception:
        return None


while True:
    # start
    get_mail()
