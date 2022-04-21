Mail Forwarder
---
Пересылка изображений во вложении электронной почты в телеграм

Установка виртуального окружиения: 
```bash
python -m venv venv
```

Активация виртуального окружения:
```bash
source venv/bin/activate
```

Установка необходимых пакетов
```bash
pip install -r requirements.txt
```

Настройка скрипта: 
Переименовать .env_example
```bash
mv .env_example .env
```
Указать логин, пароль от почты, адрес imap сервера, токен бота и ID пользователя которому необходимо направлять фото 
```bash
nano .env
```

```.env
MAIL=mail@example.com
PASSWORD=yourpassword
IMAP=imap.example.com
BOT_TOKEN=bot_tokeb
USER_ID=user_id
```

Запустить скрипт в фоне: 
```bash
nohup ./main.py &
```