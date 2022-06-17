api_id = 16852963 # Api ID From My.Telegram.Org
api_hash = '1defca4e6e118cbe0b8c9f61913a7fbf' # Api Hash From My.Telegram.Org
bot_token = '5392254683:AAGDbmAUTousvvMwkEnCgwCKuFuVPmvRk_w' # Bot Token From Bot Father
site_url = 'https://toonmixindia.me/wp-json/wp/v2/search?per_page=5&type=post&search='
from telethon.sync import TelegramClient, events
import requests
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
@bot.on(events.NewMessage)
async def my_event_handler(event):
    url2 = site_url+event.raw_text
    resp = requests.get(url=url2,)
    data = resp.json()
    lengthh = len(data)
    if lengthh > 0 :
        title1 = data[0]['title']
        url1 = data[0]['url']
        replyy = f'''{title1}\n{url1}'''
        await event.reply(replyy)
bot.start()
bot.run_until_disconnected()
