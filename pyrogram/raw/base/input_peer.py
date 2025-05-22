
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPeer = Union[raw.types.InputPeerChannel, raw.types.InputPeerChannelFromMessage, raw.types.InputPeerChat, raw.types.InputPeerEmpty, raw.types.InputPeerSelf, raw.types.InputPeerUser, raw.types.InputPeerUserFromMessage]


# noinspection PyRedeclaration
class InputPeer:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPeerChannel
            InputPeerChannelFromMessage
            InputPeerChat
            InputPeerEmpty
            InputPeerSelf
            InputPeerUser
            InputPeerUserFromMessage
    """

    QUALNAME = "pyrogram.raw.base.InputPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/input-peer")
