
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


class AttachMenuBots(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuBots`.

    Details:
        - Layer: ``166``
        - ID: ``3C4301C0``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        bots (List of :obj:`AttachMenuBot <pyrogram.raw.base.AttachMenuBot>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBots
    """

    __slots__: List[str] = ["hash", "bots", "users"]

    ID = 0x3c4301c0
    QUALNAME = "types.AttachMenuBots"

    def __init__(self, *, hash: int, bots: List["raw.base.AttachMenuBot"], users: List["raw.base.User"]) -> None:
        self.hash = hash  # long
        self.bots = bots  # Vector<AttachMenuBot>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBots":
        # No flags
        
        hash = Long.read(b)
        
        bots = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return AttachMenuBots(hash=hash, bots=bots, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.bots))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
