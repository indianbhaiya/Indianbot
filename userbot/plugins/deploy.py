"""Emoji

Available Commands:

.deploy"""

import asyncio

from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set vars from heroku"


@borg.on(admin_cmd(pattern=r"deploy"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 12)

    # input_str = event.pattern_match.group(1)

    await event.edit("Typing...")

    animation_chars = [
        "**Heroku Connecting To Latest Github Build (indianbhaiya/IndianBot)**",
        "**Build started by user** **{DEFAULTUSER}**",
        f"**Deploy** `535a74f0` **by user** **{DEFAULTUSER}**",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m stdborg`",
        "**State changed from starting to up**",
        "__INFO:IndianBot:Logged in as 557667062__",
        "__INFO:IndianBot:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])
