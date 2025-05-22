
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


class CreateChat(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``34A818``

    Parameters:
        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        title (``str``):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["users", "title", "ttl_period"]

    ID = 0x34a818
    QUALNAME = "functions.messages.CreateChat"

    def __init__(self, *, users: List["raw.base.InputUser"], title: str, ttl_period: Optional[int] = None) -> None:
        self.users = users  # Vector<InputUser>
        self.title = title  # string
        self.ttl_period = ttl_period  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateChat":
        
        flags = Int.read(b)
        
        users = TLObject.read(b)
        
        title = String.read(b)
        
        ttl_period = Int.read(b) if flags & (1 << 0) else None
        return CreateChat(users=users, title=title, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ttl_period is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.users))
        
        b.write(String(self.title))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()
