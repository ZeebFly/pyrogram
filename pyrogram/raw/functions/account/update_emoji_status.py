
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


class UpdateEmojiStatus(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``FBD3DE6B``

    Parameters:
        emoji_status (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["emoji_status"]

    ID = 0xfbd3de6b
    QUALNAME = "functions.account.UpdateEmojiStatus"

    def __init__(self, *, emoji_status: "raw.base.EmojiStatus") -> None:
        self.emoji_status = emoji_status  # EmojiStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEmojiStatus":
        # No flags
        
        emoji_status = TLObject.read(b)
        
        return UpdateEmojiStatus(emoji_status=emoji_status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.emoji_status.write())
        
        return b.getvalue()
