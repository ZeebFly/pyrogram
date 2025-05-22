
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


class MessageActionRequestedPeer(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``FE77345D``

    Parameters:
        button_id (``int`` ``32-bit``):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

    """

    __slots__: List[str] = ["button_id", "peer"]

    ID = 0xfe77345d
    QUALNAME = "types.MessageActionRequestedPeer"

    def __init__(self, *, button_id: int, peer: "raw.base.Peer") -> None:
        self.button_id = button_id  # int
        self.peer = peer  # Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionRequestedPeer":
        # No flags
        
        button_id = Int.read(b)
        
        peer = TLObject.read(b)
        
        return MessageActionRequestedPeer(button_id=button_id, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.button_id))
        
        b.write(self.peer.write())
        
        return b.getvalue()
