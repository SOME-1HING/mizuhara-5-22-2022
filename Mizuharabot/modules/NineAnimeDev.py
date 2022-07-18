# Credits to https://telegram.dog/ShalmonAnandMate

from Mizuharabot import telethn
from Mizuharabot.events import register
from telethon import Button

from animedev import client as AnimeDevClient, exceptions

@register(pattern='/search')
async def animedev_function(event):
    anime_name = event.message.message.split()
    if len(anime_name) <= 1:
        await event.reply('Please enter the anime name.\n\n<b>Example:</b>\n/search Doraemon.', parse_mode='html')
        return
    try:
        anime = AnimeDevClient.search(' '.join(anime_name[1:]))
        anime['Search_Query'] = anime['Search_Query'].replace(' ', '+')
    except exceptions.NotFound:
        await event.reply('Anime not found.')
        return
    except Exception as e:
        await event.reply(f'[ERROR]: Please report this at @Shinobu_Support.\n\nERROR:\n{e}')
        return
    msg_text = f'''
<b>Anime Title:</b> <code>{anime['AnimeTitle']}</code>
    '''
    buttons_list = [[Button.url('Download Link', anime['AnimeLink'])], [Button.url('Search Query', anime['Search_Query'])]]
    await telethn.send_file(event.chat_id, anime['AnimeImg'], caption=msg_text, buttons=buttons_list, parse_mode='html', reply_to=event.id)
