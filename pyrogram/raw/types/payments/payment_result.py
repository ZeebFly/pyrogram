
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class PaymentResult(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.PaymentResult`.

    Details:
        - Layer: ``166``
        - ID: ``4E5F810D``

    Parameters:
        updates (:obj:`Updates <pyrogram.raw.base.Updates>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.SendPaymentForm
    """

    __slots__: List[str] = ["updates"]

    ID = 0x4e5f810d
    QUALNAME = "types.payments.PaymentResult"

    def __init__(self, *, updates: "raw.base.Updates") -> None:
        self.updates = updates  # Updates

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentResult":
        # No flags
        
        updates = TLObject.read(b)
        
        return PaymentResult(updates=updates)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.updates.write())
        
        return b.getvalue()
