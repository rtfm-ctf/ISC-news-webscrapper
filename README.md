# ISC-news-webscrapper
Telegram bot to scrap daily infosec news from SANS Internet Storm Center podcast page

##Installing
```
pip install -r requirements
```

##Setup
Export the env on environ.sh.template with your bot token and chat/group id.
```
export TELEGRAM_BOT_API_TOKEN=<your bot token here>
export TELEGRAM_CHAT_GROUP_ID=<chat or group id here>

##Running
```
python ics_scrapper.py
```
