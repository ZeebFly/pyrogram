
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


class GetMessageEditData(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``FDA68D36``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.MessageEditData <pyrogram.raw.base.messages.MessageEditData>`
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0xfda68d36
    QUALNAME = "functions.messages.GetMessageEditData"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageEditData":
        # No flags
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        return GetMessageEditData(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
