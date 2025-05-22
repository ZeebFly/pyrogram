
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


class DhConfig(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.DhConfig`.

    Details:
        - Layer: ``166``
        - ID: ``2C221EDD``

    Parameters:
        g (``int`` ``32-bit``):
            N/A

        p (``bytes``):
            N/A

        version (``int`` ``32-bit``):
            N/A

        random (``bytes``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDhConfig
    """

    __slots__: List[str] = ["g", "p", "version", "random"]

    ID = 0x2c221edd
    QUALNAME = "types.messages.DhConfig"

    def __init__(self, *, g: int, p: bytes, version: int, random: bytes) -> None:
        self.g = g  # int
        self.p = p  # bytes
        self.version = version  # int
        self.random = random  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DhConfig":
        # No flags
        
        g = Int.read(b)
        
        p = Bytes.read(b)
        
        version = Int.read(b)
        
        random = Bytes.read(b)
        
        return DhConfig(g=g, p=p, version=version, random=random)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.g))
        
        b.write(Bytes(self.p))
        
        b.write(Int(self.version))
        
        b.write(Bytes(self.random))
        
        return b.getvalue()
