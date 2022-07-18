# Credits to https://telegram.dog/ShalmonAnandMate

from Mizuharabot import telethn
from Mizuharabot.events import register
from telethon import Button

from .waifuapi import WaifuClient

@register(pattern='/mywaifu')
async def my_waifu_function(event):
    waifu = WaifuClient.getRandomWaifu()
    msg_text = f'''
<b>Waifu's Name:</b> <code>{waifu['name']}</code>

<b>Waifu's Name In Kanji:</b> <code>{waifu['name_kanji']}</code>

<b>Waifu's Nicknames:</b> {'<code>' + '</code>, <code>'.join(waifu['nicknames']) + '</code>'}

<b>Waifu's About:</b>
<code>{waifu['about']}</code>
    '''
    buttons_list = [
    Button.url('My Anime List', waifu['url'])
    ]
    await telethn.send_file(event.chat_id, waifu['images']['jpg']['image_url'], caption=msg_text, buttons=buttons_list, parse_mode='html', reply_to=event.id)
