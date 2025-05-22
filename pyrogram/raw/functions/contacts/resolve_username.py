
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


class ResolveUsername(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``F93CCBA3``

    Parameters:
        username (``str``):
            N/A

    Returns:
        :obj:`contacts.ResolvedPeer <pyrogram.raw.base.contacts.ResolvedPeer>`
    """

    __slots__: List[str] = ["username"]

    ID = 0xf93ccba3
    QUALNAME = "functions.contacts.ResolveUsername"

    def __init__(self, *, username: str) -> None:
        self.username = username  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolveUsername":
        # No flags
        
        username = String.read(b)
        
        return ResolveUsername(username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.username))
        
        return b.getvalue()
