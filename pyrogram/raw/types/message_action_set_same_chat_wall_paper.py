
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


class MessageActionSetSameChatWallPaper(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``C0787D6D``

    Parameters:
        wallpaper (:obj:`WallPaper <pyrogram.raw.base.WallPaper>`):
            N/A

    """

    __slots__: List[str] = ["wallpaper"]

    ID = 0xc0787d6d
    QUALNAME = "types.MessageActionSetSameChatWallPaper"

    def __init__(self, *, wallpaper: "raw.base.WallPaper") -> None:
        self.wallpaper = wallpaper  # WallPaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetSameChatWallPaper":
        # No flags
        
        wallpaper = TLObject.read(b)
        
        return MessageActionSetSameChatWallPaper(wallpaper=wallpaper)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.wallpaper.write())
        
        return b.getvalue()
