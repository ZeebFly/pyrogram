
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PhoneCallDiscardReason = Union[raw.types.PhoneCallDiscardReasonBusy, raw.types.PhoneCallDiscardReasonDisconnect, raw.types.PhoneCallDiscardReasonHangup, raw.types.PhoneCallDiscardReasonMissed]


# noinspection PyRedeclaration
class PhoneCallDiscardReason:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PhoneCallDiscardReasonBusy
            PhoneCallDiscardReasonDisconnect
            PhoneCallDiscardReasonHangup
            PhoneCallDiscardReasonMissed
    """

    QUALNAME = "pyrogram.raw.base.PhoneCallDiscardReason"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/phone-call-discard-reason")
