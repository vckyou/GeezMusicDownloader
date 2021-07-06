"""
✘ Commands Available -
• `{i}getmembers`
    Scraping Member from a Chat.
• `{i}addmembers`
    Adding Member to a Chat.
• First you must do {i}getmembers first from a Chat. Then go to your group and type {i}addmembers for adding them to your group.
"""


import asyncio
import csv
import random
import traceback

from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserPrivacyRestrictedError,
    UserNotMutualContactError
)

from . import *
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser


@ultroid_cmd(pattern="getmembers")
async def scrapmem(event):
    chat = event.chat_id
    y = await eor(event, "`Please wait...`")
    client = event.client
    members = await client.get_participants(chat, aggressive=True)

    with open("members.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(["user_id", "hash"])
        for member in members:
            writer.writerow([member.id, member.access_hash])
    await eor(y, "`Members scraped.`")


@ultroid_cmd(pattern="addmembers")
async def admem(event):
    x = await eor(event, "`Adding 0 members...`")
    chat = await event.get_chat()
    client = event.client
    users = []
    with open("members.csv", encoding="UTF-8") as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {'id': int(row[0]), 'hash': int(row[1])}
            users.append(user)
    n = 0
    for user in users:
        n += 1
        if n % 30 == 0:
            await eor(x, f"`Reached 30 members, sleeping for {900/60} minutes`")
            await asyncio.sleep(900)
        try:
            userin = InputPeerUser(user['id'], user['hash'])
            await client(InviteToChannelRequest(chat, [userin]))
            await asyncio.sleep(random.randrange(5, 7))
            await eor(x, f"`Adding {n} members...`")
        except TypeError:
            n -= 1
            continue
        except UserAlreadyParticipantError:
            n -= 1
            continue
        except UserPrivacyRestrictedError:
            n -= 1
            continue
        except UserNotMutualContactError:
            n -= 1
            continue
