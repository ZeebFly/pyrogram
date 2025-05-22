
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

KeyboardButton = Union[raw.types.InputKeyboardButtonUrlAuth, raw.types.InputKeyboardButtonUserProfile, raw.types.KeyboardButton, raw.types.KeyboardButtonBuy, raw.types.KeyboardButtonCallback, raw.types.KeyboardButtonGame, raw.types.KeyboardButtonRequestGeoLocation, raw.types.KeyboardButtonRequestPeer, raw.types.KeyboardButtonRequestPhone, raw.types.KeyboardButtonRequestPoll, raw.types.KeyboardButtonSimpleWebView, raw.types.KeyboardButtonSwitchInline, raw.types.KeyboardButtonUrl, raw.types.KeyboardButtonUrlAuth, raw.types.KeyboardButtonUserProfile, raw.types.KeyboardButtonWebView, raw.types.KeyboardButtonCopy]


# noinspection PyRedeclaration
class KeyboardButton:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 16 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputKeyboardButtonUrlAuth
            InputKeyboardButtonUserProfile
            KeyboardButton
            KeyboardButtonBuy
            KeyboardButtonCallback
            KeyboardButtonGame
            KeyboardButtonRequestGeoLocation
            KeyboardButtonRequestPeer
            KeyboardButtonRequestPhone
            KeyboardButtonRequestPoll
            KeyboardButtonSimpleWebView
            KeyboardButtonSwitchInline
            KeyboardButtonUrl
            KeyboardButtonUrlAuth
            KeyboardButtonUserProfile
            KeyboardButtonWebView
            KeyboardButtonCopy
    """

    QUALNAME = "pyrogram.raw.base.KeyboardButton"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/keyboard-button")
