from typing import List

from pyrogram.types import Chat

from MusicUserbot.helpers.get_admins import get as gett
from MusicUserbot.helpers.get_admins import set as sett


async def get_administrators(chat: Chat) -> List[int]:
    get = gett(chat.id)

    if get:
        return get
    else:
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        sett(chat.id, to_set)
        return await get_administrators(chat)
