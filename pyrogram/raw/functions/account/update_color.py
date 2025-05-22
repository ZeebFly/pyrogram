
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


class UpdateColor(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``A001CC43``

    Parameters:
        color (``int`` ``32-bit``):
            N/A

        background_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["color", "background_emoji_id"]

    ID = 0xa001cc43
    QUALNAME = "functions.account.UpdateColor"

    def __init__(self, *, color: int, background_emoji_id: Optional[int] = None) -> None:
        self.color = color  # int
        self.background_emoji_id = background_emoji_id  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateColor":
        
        flags = Int.read(b)
        
        color = Int.read(b)
        
        background_emoji_id = Long.read(b) if flags & (1 << 0) else None
        return UpdateColor(color=color, background_emoji_id=background_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.background_emoji_id is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.color))
        
        if self.background_emoji_id is not None:
            b.write(Long(self.background_emoji_id))
        
        return b.getvalue()
