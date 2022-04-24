from email import message
from hashlib import new
from telethon.sync import TelegramClient, events
api_id = 16852963
api_hash = '1defca4e6e118cbe0b8c9f61913a7fbf'
bot_token = '5392254683:AAGDbmAUTousvvMwkEnCgwCKuFuVPmvRk_w'
import requests

prousers = [2054876812,1479609725,]

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
@bot.on(events.NewMessage)
async def my_event_handler(event):
    # if 'tmi' in event.raw_text:
    newtxt =event.raw_text
    ids = event.chat_id
    print(type(type(event.entities)))
    if type(event.entities) == list :
        if event.message.peer_id.user_id in prousers :
            pass
        else :
            await bot.delete_messages(ids,event.message.id)
    else :
        pass
    if ids == -1001445924604 :
        url = 'https://toonmixindia.me/wp-json/wp/v2/search?per_page=5&type=post&search='
    else :
        url = 'https://coolsanime.me/wp-json/wp/v2/search?per_page=5&type=post&search='
    # y = newtxt.replace('tmi ','')
    y = newtxt
    url2 = url+y
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