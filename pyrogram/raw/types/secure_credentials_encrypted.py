
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


class SecureCredentialsEncrypted(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureCredentialsEncrypted`.

    Details:
        - Layer: ``166``
        - ID: ``33F0EA47``

    Parameters:
        data (``bytes``):
            N/A

        hash (``bytes``):
            N/A

        secret (``bytes``):
            N/A

    """

    __slots__: List[str] = ["data", "hash", "secret"]

    ID = 0x33f0ea47
    QUALNAME = "types.SecureCredentialsEncrypted"

    def __init__(self, *, data: bytes, hash: bytes, secret: bytes) -> None:
        self.data = data  # bytes
        self.hash = hash  # bytes
        self.secret = secret  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureCredentialsEncrypted":
        # No flags
        
        data = Bytes.read(b)
        
        hash = Bytes.read(b)
        
        secret = Bytes.read(b)
        
        return SecureCredentialsEncrypted(data=data, hash=hash, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.data))
        
        b.write(Bytes(self.hash))
        
        b.write(Bytes(self.secret))
        
        return b.getvalue()
