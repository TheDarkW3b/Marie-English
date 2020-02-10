from telegram import ChatActionimport htmlimport urllib.requestimport reimport jsonfrom typing import Optional, Listimport timeimport urllibfrom urllib.request import urlopen, urlretrievefrom urllib.parse import quote_plus, urlencodeimport requestsfrom telegram import Message, Chat, Update, Bot, MessageEntityfrom telegram import ParseModefrom telegram.ext import CommandHandler, run_async, Filtersfrom tg_bot.modules.helper_funcs.filters import CustomFiltersfrom tg_bot import dispatcherfrom tg_bot.__main__ import STATS, USER_INFO
from tg_bot.modules.translations.strings import tld def proxy(bot: Bot, update: Update): proxy = requests.get('https://proxy11.com/api/proxy.json?key=OTA4.XkBkMw.kXAnDeXngEOrMlYcQ65ueOewBCY').json()[0]["preview"] final = "https://proxy11.com/{}".format(proxy) update.message.reply_text(tld(final)
return ""	

__help__ = """ - * Only For Sudos Now * - /proxy: Get Updated Proxy list"""

__mod_name__ = "PROXY"
	PROXY_HANDLER = CommandHandler("proxy", Proxy, filters=CustomFilters.sudo_filter)dispatcher.add_handler(PROXY_HANDLER)