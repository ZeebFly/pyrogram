
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotCommandScope = Union[raw.types.BotCommandScopeChatAdmins, raw.types.BotCommandScopeChats, raw.types.BotCommandScopeDefault, raw.types.BotCommandScopePeer, raw.types.BotCommandScopePeerAdmins, raw.types.BotCommandScopePeerUser, raw.types.BotCommandScopeUsers]


# noinspection PyRedeclaration
class BotCommandScope:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotCommandScopeChatAdmins
            BotCommandScopeChats
            BotCommandScopeDefault
            BotCommandScopePeer
            BotCommandScopePeerAdmins
            BotCommandScopePeerUser
            BotCommandScopeUsers
    """

    QUALNAME = "pyrogram.raw.base.BotCommandScope"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/bot-command-scope")
