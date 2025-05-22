
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


class InputReplyToStory(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputReplyTo`.

    Details:
        - Layer: ``166``
        - ID: ``15B0F283``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        story_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "story_id"]

    ID = 0x15b0f283
    QUALNAME = "types.InputReplyToStory"

    def __init__(self, *, user_id: "raw.base.InputUser", story_id: int) -> None:
        self.user_id = user_id  # InputUser
        self.story_id = story_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReplyToStory":
        # No flags
        
        user_id = TLObject.read(b)
        
        story_id = Int.read(b)
        
        return InputReplyToStory(user_id=user_id, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Int(self.story_id))
        
        return b.getvalue()
