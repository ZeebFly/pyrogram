
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


class UpdateStatus(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``6628562C``

    Parameters:
        offline (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["offline"]

    ID = 0x6628562c
    QUALNAME = "functions.account.UpdateStatus"

    def __init__(self, *, offline: bool) -> None:
        self.offline = offline  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStatus":
        # No flags
        
        offline = Bool.read(b)
        
        return UpdateStatus(offline=offline)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bool(self.offline))
        
        return b.getvalue()
