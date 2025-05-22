
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


class CheckedGiftCode(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.CheckedGiftCode`.

    Details:
        - Layer: ``166``
        - ID: ``B722F158``

    Parameters:
        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        months (``int`` ``32-bit``):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        via_giveaway (``bool``, *optional*):
            N/A

        giveaway_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        to_id (``int`` ``64-bit``, *optional*):
            N/A

        used_date (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.CheckGiftCode
    """

    __slots__: List[str] = ["from_id", "date", "months", "chats", "users", "via_giveaway", "giveaway_msg_id", "to_id", "used_date"]

    ID = 0xb722f158
    QUALNAME = "types.payments.CheckedGiftCode"

    def __init__(self, *, from_id: "raw.base.Peer", date: int, months: int, chats: List["raw.base.Chat"], users: List["raw.base.User"], via_giveaway: Optional[bool] = None, giveaway_msg_id: Optional[int] = None, to_id: Optional[int] = None, used_date: Optional[int] = None) -> None:
        self.from_id = from_id  # Peer
        self.date = date  # int
        self.months = months  # int
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.via_giveaway = via_giveaway  # flags.2?true
        self.giveaway_msg_id = giveaway_msg_id  # flags.3?int
        self.to_id = to_id  # flags.0?long
        self.used_date = used_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckedGiftCode":
        
        flags = Int.read(b)
        
        via_giveaway = True if flags & (1 << 2) else False
        from_id = TLObject.read(b)
        
        giveaway_msg_id = Int.read(b) if flags & (1 << 3) else None
        to_id = Long.read(b) if flags & (1 << 0) else None
        date = Int.read(b)
        
        months = Int.read(b)
        
        used_date = Int.read(b) if flags & (1 << 1) else None
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return CheckedGiftCode(from_id=from_id, date=date, months=months, chats=chats, users=users, via_giveaway=via_giveaway, giveaway_msg_id=giveaway_msg_id, to_id=to_id, used_date=used_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.via_giveaway else 0
        flags |= (1 << 3) if self.giveaway_msg_id is not None else 0
        flags |= (1 << 0) if self.to_id is not None else 0
        flags |= (1 << 1) if self.used_date is not None else 0
        b.write(Int(flags))
        
        b.write(self.from_id.write())
        
        if self.giveaway_msg_id is not None:
            b.write(Int(self.giveaway_msg_id))
        
        if self.to_id is not None:
            b.write(Long(self.to_id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.months))
        
        if self.used_date is not None:
            b.write(Int(self.used_date))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
