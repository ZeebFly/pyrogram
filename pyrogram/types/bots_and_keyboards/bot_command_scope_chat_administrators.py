
from typing import Union

import pyrogram
from pyrogram import raw
from .bot_command_scope import BotCommandScope


class BotCommandScopeChatAdministrators(BotCommandScope):
    """Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

    Parameters:
        chat_id (``int`` | ``str``):
            Unique identifier for the target chat or username of the target supergroup (in the format
            @supergroupusername).
    """

    def __init__(self, chat_id: Union[int, str]):
        super().__init__("chat_administrators")

        self.chat_id = chat_id

    async def write(self, client: "pyrogram.Client") -> "raw.base.BotCommandScope":
        return raw.types.BotCommandScopePeerAdmins(
            peer=await client.resolve_peer(self.chat_id)
        )
