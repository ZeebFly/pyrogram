
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


class SecureValueErrorFiles(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``166``
        - ID: ``666220E9``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

        file_hash (List of ``bytes``):
            N/A

        text (``str``):
            N/A

    """

    __slots__: List[str] = ["type", "file_hash", "text"]

    ID = 0x666220e9
    QUALNAME = "types.SecureValueErrorFiles"

    def __init__(self, *, type: "raw.base.SecureValueType", file_hash: List[bytes], text: str) -> None:
        self.type = type  # SecureValueType
        self.file_hash = file_hash  # Vector<bytes>
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorFiles":
        # No flags
        
        type = TLObject.read(b)
        
        file_hash = TLObject.read(b, Bytes)
        
        text = String.read(b)
        
        return SecureValueErrorFiles(type=type, file_hash=file_hash, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.type.write())
        
        b.write(Vector(self.file_hash, Bytes))
        
        b.write(String(self.text))
        
        return b.getvalue()
