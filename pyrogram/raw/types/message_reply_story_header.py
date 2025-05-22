
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


class MessageReplyStoryHeader(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageReplyHeader`.

    Details:
        - Layer: ``166``
        - ID: ``9C98BFC1``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        story_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "story_id"]

    ID = 0x9c98bfc1
    QUALNAME = "types.MessageReplyStoryHeader"

    def __init__(self, *, user_id: int, story_id: int) -> None:
        self.user_id = user_id  # long
        self.story_id = story_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReplyStoryHeader":
        # No flags
        
        user_id = Long.read(b)
        
        story_id = Int.read(b)
        
        return MessageReplyStoryHeader(user_id=user_id, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.story_id))
        
        return b.getvalue()
