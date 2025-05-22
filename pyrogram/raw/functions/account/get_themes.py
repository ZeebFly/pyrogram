
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


class GetThemes(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``7206E458``

    Parameters:
        format (``str``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`account.Themes <pyrogram.raw.base.account.Themes>`
    """

    __slots__: List[str] = ["format", "hash"]

    ID = 0x7206e458
    QUALNAME = "functions.account.GetThemes"

    def __init__(self, *, format: str, hash: int) -> None:
        self.format = format  # string
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetThemes":
        # No flags
        
        format = String.read(b)
        
        hash = Long.read(b)
        
        return GetThemes(format=format, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
