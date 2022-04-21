# !/usr/bin/env python
# -*- coding: utf-8 -*-

from imap_tools import MailBox, AND, A
import imap_tools
import telebot


def read_config():
    with open('.env', 'r') as f:
        config = dict(
            tuple(line.replace('\n', '').split('='))
            for line in f.readlines() if not line.startswith('#')
        )
    f.close()
    return config


def get_mail():
    config = read_config()
    server = config['IMAP']
    login = config['MAIL']
    pwd = config['PASSWORD']
    bot_token = config['BOT_TOKEN']
    user_id = config['USER_ID']
    bot = telebot.TeleBot(bot_token)
    try:
        mailbox = MailBox(server).login(login, pwd)
        for msg in mailbox.fetch(A(seen=False)):
            for att in msg.attachments:
                img = att.payload
                bot.send_photo(user_id, img)
        flags = imap_tools.MailMessageFlags.SEEN
        mailbox.flag(mailbox.uids(AND(seen=True)), flags, True)
        mailbox.logout()
        return None
    except Exception:
        return None


while True:
    #start
    get_mail()
