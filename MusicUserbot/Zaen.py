from random import randint
from pyrogram import Client, filters
from config import HNDLR, bot as USER
from MusicUserbot.helpers.decorators import authorized_users_only
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.raw.functions.phone import CreateGroupCall


@Client.on_message(filters.command(["join"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def join(client, message):
    chat_id = message.chat.id
    try:
        link = await client.export_chat_invite_link(chat_id)
    except Exception:
        await message.reply("**Error:**\nAdd me as an admin of your group.")
        return
    try:
        await USER.join_chat(link)
        await message.reply("**Userbot joined the group.**")
    except UserAlreadyParticipant:
        await message.reply("**Userbot already joined this group.**")


@Client.on_message(filters.command(["openvcs"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def opengc(client, message):
    flags = " ".join(message.command[1:])
    if flags == "channel":
        chat_id = message.chat.username
        type = "channel"
    else:
        chat_id = message.chat.id
        type = "group"
    try:
        await USER.send(CreateGroupCall(
            peer=(await USER.resolve_peer(chat_id)),
            random_id=randint(10000, 999999999),
            participants=[
                await USER.resolve_peer(user_id)
                for user_id in await client.get_participants(chat_id)
            ]
        )
        )
    except Exception:
        await message.reply(
            "**Error:** Add userbot as admin of your group/channel with permission **Can manage voice chat**."
        )
