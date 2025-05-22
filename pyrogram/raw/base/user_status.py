
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

UserStatus = Union[raw.types.UserStatusEmpty, raw.types.UserStatusLastMonth, raw.types.UserStatusLastWeek, raw.types.UserStatusOffline, raw.types.UserStatusOnline, raw.types.UserStatusRecently]


# noinspection PyRedeclaration
class UserStatus:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            UserStatusEmpty
            UserStatusLastMonth
            UserStatusLastWeek
            UserStatusOffline
            UserStatusOnline
            UserStatusRecently
    """

    QUALNAME = "pyrogram.raw.base.UserStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/user-status")
