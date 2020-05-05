
Available Commands:
.spower
Credits to @pureindialover
"""

from telethon import events
import asyncio
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from userbot import CHANNEL

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @IndianBot_Official"
CHANNEL = str(CHANNEL) if CHANNEL else "@IndianBot_Official"

@borg.on(admin_cmd("spower"))
async def _(event):
    if event.fwd_from:
        return
    elif not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("{DEFAULTUSER} tera baap")
        await asyncio.sleep(0.2)
        await event.edit("{DEFAULTUSER} bot ko jaan dene wala")
        await asyncio.sleep(0.2)
        await event.edit("{DEFAULTUSER} husband of ur mummy")
        await asyncio.sleep(0.2)
        await event.edit("{DEFAULTUSER} user at {CHANNEL}")
        await asyncio.sleep(0.2)
        await event.edit("Tujhe aur kya chaiye @pureindialover is with me")
        await asyncio.sleep(0.2)
        await event.edit("tera baap")
        await asyncio.sleep(0.2)
        await event.edit("{DEFAULTUSER}")
