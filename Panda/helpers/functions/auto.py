from Panda.sql_helper.globals import gvarstatus, addgvar
from Panda import PandaBot as mansizbot
import asyncio
from urllib.request import urlretrieve


import os
from random import randint
from urllib.request import urlretrieve
import heroku3
from telethon.tl.functions.users import GetFullUserRequest
from decouple import config
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


from telethon.errors.rpcerrorlist import ChannelsTooMuchError
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    JoinChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatAdminRights,
    InputChatUploadedPhoto,
    InputMessagesFilterDocument,
)

try:
    import aiofiles
    import aiohttp
except ImportError:
    import urllib

    aiohttp = None

async def download_file(link, name):
    """for files, without progress callback with aiohttp"""
    if not aiohttp:
        urllib.request.urlretrieve(link, name)
        return name
    async with aiohttp.ClientSession() as ses:
        async with ses.get(link) as re_ses:
            file = await aiofiles.open(name, "wb")
            await file.write(await re_ses.read())
            await file.close()
    return name


BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", None)
LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)




async def autogrup():
    await mansizbot.start()
    if LOG_CHANNEL:
        (LOG_CHANNEL, str(LOG_CHANNEL))
        return
    if Var.LOG_CHANNEL:
        return
    LOGS.info("🛠 MEMBUAT Grup Pribadi HARAP TUNGU !!")
    try:
        r = await mansizbot(
            CreateChannelRequest(
                title="🛠 BOTLOG & SETTING 🛠",
                about="Ini adalah sebuah grup yang dibuat otomatis untuk mengatur bot saat erorr ...\n\n Join @TeamSquadUserbotSuport",
                megagroup=True,
            ),
        )
    except ChannelsTooMuchError:
        LOGS.info(
            "You Are in Too Many Channels & Groups , Leave some And Restart The Bot"
        )
        exit(1)
    except BaseException as er:
        LOGS.info(er)
        LOGS.info(
            "Something Went Wrong , Create A Group and set its id on config var LOG_CHANNEL."
        )
        exit(1)
    rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        anonymous=False,
        manage_call=True,
    )
    chat = r.chats[0]
    chat_id = chat.id
    await mansizbot(EditAdminRequest(chat_id, TG_BOT_USERNAME, rights, "Assistant"))
    photo = await download_file(
        "https://telegra.ph/file/da037f0eaeaa1423eea49.jpg", "channelphoto.jpg"
    )
    ll = await mansizbot.upload_file(photo)
    await mansizbot(EditPhotoRequest(chat_id, InputChatUploadedPhoto(ll)))
    os.remove(photo)
    if not str(chat_id).startswith("-100"):
        LOGBOT = gvarstatus(BOTLOG) or "-100" + str(chat_id)
    else:
        LOGBOT = gvarstatus(BOTLOG) or str(chat_id)





async def autobot():
    await mansizbot.start()
    if BOT_TOKEN:
        (BOT_TOKEN, str(BOT_TOKEN))
        return
    if BOT_TOKEN:
        return
    LOGS.info("🛠 MEMBUAT BOT UNTUK ANDA DI @BotFather, HARAP TUNGU !!")
    who = await mansizbot.get_me()
    name = "Assistant " + who.first_name
    if who.username:
        username = who.username + "_Pandabot"
    else:
        username = "PandaX_Userbot_" + (str(who.id))[5:] + "_bot"
    bf = "Botfather"
    await mansizbot(UnblockRequest(bf))
    await mansizbot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await mansizbot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await mansizbot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await mansizbot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Mohon buat bot baru di @BotFather dan tambahkan var BOT_TOKEN, lalu isi token nya dan restart."
        )
        exit(1)
    await mansizbot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await mansizbot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await mansizbot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await mansizbot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Mohon buat bot baru di @BotFather dan tambahkan var BOT_TOKEN, lalu isi token nya dan restart."
            )
            exit(1)
    await mansizbot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await mansizbot.get_messages(bf, limit=1))[0].text
    await mansizbot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "PandaX_Userbot" + (str(who.id))[6:] + str(ran) + "_bot"
        await mansizbot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await mansizbot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            await mansizbot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await mansizbot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await mansizbot.send_message(bf, "menu...")
            await asyncio.sleep(3)
            await mansizbot.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await mansizbot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await mansizbot.send_file(bf, "PandaVersion/Panda/pandaasis.jpg")
            await asyncio.sleep(2)
            await mansizbot.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await mansizbot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await mansizbot.send_message(
            bf, f"🙋 Hello ✨ Saya PandaX_Userbot Assistant"
            )
            await asyncio.sleep(2)
            await mansizbot.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await mansizbot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await mansizbot.send_message(
            bf, f"PandaX_Userbot Assistant\n\nBy ~ @diemmmmmmmmmm\nSupport ~ @TEAMSquadUserbotSupport ",
            )
            TOKENBOT = gvarstatus(TOKENBOT) or token
            USERBOT = gvarstatus(USERBOT) or f"@{username}"
            LOGS.info(f"SELESAI, ASSISTANT BOT ANDA SUDAH DIBUAT @{username}")
        else:
            LOGS.info(
                f"Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot."
            )
            exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        await mansizbot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await mansizbot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await mansizbot.send_message(bf, "menu...")
        await asyncio.sleep(3)
        await mansizbot.send_message(bf, "/setuserpic")
        await asyncio.sleep(1)
        await mansizbot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await mansizbot.send_file(bf, "PandaVersion/Panda/pandaasis.jpg")
        await asyncio.sleep(1)
        await mansizbot.send_message(bf, "/setabouttext")
        await asyncio.sleep(1)
        await mansizbot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await mansizbot.send_message(
        bf, f"🙋 Hello ✨ Saya PandaX_Userbot Assistant"
        )
        await asyncio.sleep(2)
        await mansizbot.send_message(bf, "/setdescription")
        await asyncio.sleep(1)
        await mansizbot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await mansizbot.send_message(
        bf, f"PandaX_Userbot Assistant\n\nBy ~ @diemmmmmmmmmm\nSupport ~ @TEAMSquadUserbotSupport ",
        )
        TOKENBOT = gvarstatus(TOKENBOT) or token
        USERBOT = gvarstatus(USERBOT) or f"@{username}"
        LOGS.info(f"SELESAI, ASSISTANT BOT ANDA SUDAH DIBUAT @{username}")
    else:
        LOGS.info(
            f"Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot."
        )
        exit(1)