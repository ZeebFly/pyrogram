
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


class DeleteByPhones(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``1013FD9E``

    Parameters:
        phones (List of ``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phones"]

    ID = 0x1013fd9e
    QUALNAME = "functions.contacts.DeleteByPhones"

    def __init__(self, *, phones: List[str]) -> None:
        self.phones = phones  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteByPhones":
        # No flags
        
        phones = TLObject.read(b, String)
        
        return DeleteByPhones(phones=phones)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.phones, String))
        
        return b.getvalue()
