
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


class PrepaidGiveaway(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PrepaidGiveaway`.

    Details:
        - Layer: ``166``
        - ID: ``B2539D54``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        months (``int`` ``32-bit``):
            N/A

        quantity (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "months", "quantity", "date"]

    ID = 0xb2539d54
    QUALNAME = "types.PrepaidGiveaway"

    def __init__(self, *, id: int, months: int, quantity: int, date: int) -> None:
        self.id = id  # long
        self.months = months  # int
        self.quantity = quantity  # int
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrepaidGiveaway":
        # No flags
        
        id = Long.read(b)
        
        months = Int.read(b)
        
        quantity = Int.read(b)
        
        date = Int.read(b)
        
        return PrepaidGiveaway(id=id, months=months, quantity=quantity, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Int(self.months))
        
        b.write(Int(self.quantity))
        
        b.write(Int(self.date))
        
        return b.getvalue()
