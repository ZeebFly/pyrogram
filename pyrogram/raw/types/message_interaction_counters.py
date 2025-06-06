
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


class MessageInteractionCounters(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageInteractionCounters`.

    Details:
        - Layer: ``166``
        - ID: ``AD4FC9BD``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        views (``int`` ``32-bit``):
            N/A

        forwards (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["msg_id", "views", "forwards"]

    ID = 0xad4fc9bd
    QUALNAME = "types.MessageInteractionCounters"

    def __init__(self, *, msg_id: int, views: int, forwards: int) -> None:
        self.msg_id = msg_id  # int
        self.views = views  # int
        self.forwards = forwards  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageInteractionCounters":
        # No flags
        
        msg_id = Int.read(b)
        
        views = Int.read(b)
        
        forwards = Int.read(b)
        
        return MessageInteractionCounters(msg_id=msg_id, views=views, forwards=forwards)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.views))
        
        b.write(Int(self.forwards))
        
        return b.getvalue()
