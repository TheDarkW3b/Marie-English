from telegram import ChatAction
import html
import urllib.request
import reimport json
from typing import Optional, List
import time
import urllib
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote_plus, urlencode
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from tg_bot.modules.helper_funcs.filters import CustomFilters
from tg_bot import dispatcher
from tg_bot.__main__ import STATS, USER_INFO
from tg_bot.modules.translations.strings import tld

@run_async
def proxy(bot: Bot, update: Update): 
	proxy = requests.get('https://proxy11.com/api/proxy.json?key=OTA4.XkBkMw.kXAnDeXngEOrMlYcQ65ueOewBCY').json()[0]["preview"] 
	final = "https://proxy11.com/{}".format(proxy) update.message.reply_text(tld(final)
return ""	

__help__ = """ - * Only For Sudos Now * - /proxy: Get Updated Proxy list"""

__mod_name__ = "PROXY"
	PROXY_HANDLER = CommandHandler("proxy", Proxy, filters=CustomFilters.sudo_filter)dispatcher.add_handler(PROXY_HANDLER)
