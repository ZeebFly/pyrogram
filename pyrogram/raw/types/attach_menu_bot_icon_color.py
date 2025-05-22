
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


class AttachMenuBotIconColor(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuBotIconColor`.

    Details:
        - Layer: ``166``
        - ID: ``4576F3F0``

    Parameters:
        name (``str``):
            N/A

        color (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["name", "color"]

    ID = 0x4576f3f0
    QUALNAME = "types.AttachMenuBotIconColor"

    def __init__(self, *, name: str, color: int) -> None:
        self.name = name  # string
        self.color = color  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotIconColor":
        # No flags
        
        name = String.read(b)
        
        color = Int.read(b)
        
        return AttachMenuBotIconColor(name=name, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.name))
        
        b.write(Int(self.color))
        
        return b.getvalue()
