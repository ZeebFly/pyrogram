
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


class GiveawayInfoResults(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.GiveawayInfo`.

    Details:
        - Layer: ``166``
        - ID: ``CD5570``

    Parameters:
        start_date (``int`` ``32-bit``):
            N/A

        finish_date (``int`` ``32-bit``):
            N/A

        winners_count (``int`` ``32-bit``):
            N/A

        activated_count (``int`` ``32-bit``):
            N/A

        winner (``bool``, *optional*):
            N/A

        refunded (``bool``, *optional*):
            N/A

        gift_code_slug (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetGiveawayInfo
    """

    __slots__: List[str] = ["start_date", "finish_date", "winners_count", "activated_count", "winner", "refunded", "gift_code_slug"]

    ID = 0xcd5570
    QUALNAME = "types.payments.GiveawayInfoResults"

    def __init__(self, *, start_date: int, finish_date: int, winners_count: int, activated_count: int, winner: Optional[bool] = None, refunded: Optional[bool] = None, gift_code_slug: Optional[str] = None) -> None:
        self.start_date = start_date  # int
        self.finish_date = finish_date  # int
        self.winners_count = winners_count  # int
        self.activated_count = activated_count  # int
        self.winner = winner  # flags.0?true
        self.refunded = refunded  # flags.1?true
        self.gift_code_slug = gift_code_slug  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GiveawayInfoResults":
        
        flags = Int.read(b)
        
        winner = True if flags & (1 << 0) else False
        refunded = True if flags & (1 << 1) else False
        start_date = Int.read(b)
        
        gift_code_slug = String.read(b) if flags & (1 << 0) else None
        finish_date = Int.read(b)
        
        winners_count = Int.read(b)
        
        activated_count = Int.read(b)
        
        return GiveawayInfoResults(start_date=start_date, finish_date=finish_date, winners_count=winners_count, activated_count=activated_count, winner=winner, refunded=refunded, gift_code_slug=gift_code_slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.winner else 0
        flags |= (1 << 1) if self.refunded else 0
        flags |= (1 << 0) if self.gift_code_slug is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.start_date))
        
        if self.gift_code_slug is not None:
            b.write(String(self.gift_code_slug))
        
        b.write(Int(self.finish_date))
        
        b.write(Int(self.winners_count))
        
        b.write(Int(self.activated_count))
        
        return b.getvalue()
