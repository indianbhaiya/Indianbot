"""Emoji
Available Commands:
.pureindialover
Credits to @pureindialover
"""
import asyncio

from telethon import events

from userbot.utils import admin_cmd


@borg.on(admin_cmd("pureindialover"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "pureindialover":
    await event.edit("@pureindialover")
    animation_chars = [
        "@pureindialover mera Loda",
        "@pureindialover Randi ka baccha",
        "@pureindialover Apni Ma chod ke apne bhai ko jan dene wala",
        "@pureindialover owner of @Randi_hu_mai Army ",
        "Loda Aur Lund Nahi Hai mere Pas",
        "Mere Baap Ka loda chahiye mujhko",
        "@pureindialover",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
