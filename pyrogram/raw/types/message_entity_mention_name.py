
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


class MessageEntityMentionName(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``166``
        - ID: ``DC7B1140``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["offset", "length", "user_id"]

    ID = 0xdc7b1140
    QUALNAME = "types.MessageEntityMentionName"

    def __init__(self, *, offset: int, length: int, user_id: int) -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityMentionName":
        # No flags
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        user_id = Long.read(b)
        
        return MessageEntityMentionName(offset=offset, length=length, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(Long(self.user_id))
        
        return b.getvalue()
