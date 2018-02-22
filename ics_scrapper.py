from bs4 import BeautifulSoup
import re
import requests 
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler

url = "https://isc.sans.edu/podcast.html"
chat = os.environ.get('TELEGRAM_CHAT_GROUP_ID') 
updater = Updater(token=os.environ.get('TELEGRAM_BOT_API_TOKEN'))
dispatcher = updater.dispatcher

def news(bot,update):
	req = requests.get(url)
	page_soup = BeautifulSoup(req.text, "html.parser")
	string = page_soup.blockquote
	pattern = (r'(<blockquote>\n)(.*?)(<br\/> <a href=\")(.*?)(\".*?<br/><br/>)(.*?)(.*?)(<br\/> <a href=\")(.*?)(\".*?<br/><br/>)(.*?)(<br/> <a href=\")(.*?)(\".*?)(\n</blockquote>)')
	m = re.match(pattern, str(string))
	msg =  ('1. '+ m.group(2))
	msg += ('\n    '+ m.group(4))
	bot.send_message(chat_id=chat, text=msg)
	msg = ('2. '+ m.group(7))
	msg += ('\n    '+ m.group(9))
	bot.send_message(chat_id=chat, text=msg)
	msg = ('3. '+ m.group(11))
	msg += ('\n    '+ m.group(13))
	bot.send_message(chat_id=chat, text=msg)

news_handler = CommandHandler('news', news)
dispatcher.add_handler(news_handler)
updater.start_polling()

