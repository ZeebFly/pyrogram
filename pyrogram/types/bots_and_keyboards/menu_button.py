
import pyrogram
from pyrogram import raw
from ..object import Object


class MenuButton(Object):
    """Describes the bot's menu button in a private chat.

    It should be one of:

    - :obj:`~pyrogram.types.MenuButtonCommands`
    - :obj:`~pyrogram.types.MenuButtonWebApp`
    - :obj:`~pyrogram.types.MenuButtonDefault`

    If a menu button other than :obj:`~pyrogram.types.MenuButtonDefault` is set for a private chat, then it is applied
    in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot
    commands.
    """

    def __init__(self, type: str):
        super().__init__()

        self.type = type

    async def write(self, client: "pyrogram.Client") -> "raw.base.BotMenuButton":
        raise NotImplementedError
