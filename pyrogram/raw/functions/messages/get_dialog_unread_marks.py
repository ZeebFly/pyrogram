
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


class GetDialogUnreadMarks(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``22E24E22``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`
    """

    __slots__: List[str] = []

    ID = 0x22e24e22
    QUALNAME = "functions.messages.GetDialogUnreadMarks"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDialogUnreadMarks":
        # No flags
        
        return GetDialogUnreadMarks()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
