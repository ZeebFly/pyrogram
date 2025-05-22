
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


class UpdateMessageReactions(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``166``
        - ID: ``5E1B3CB8``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        reactions (:obj:`MessageReactions <pyrogram.raw.base.MessageReactions>`):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "msg_id", "reactions", "top_msg_id"]

    ID = 0x5e1b3cb8
    QUALNAME = "types.UpdateMessageReactions"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, reactions: "raw.base.MessageReactions", top_msg_id: Optional[int] = None) -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.reactions = reactions  # MessageReactions
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessageReactions":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        reactions = TLObject.read(b)
        
        return UpdateMessageReactions(peer=peer, msg_id=msg_id, reactions=reactions, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(self.reactions.write())
        
        return b.getvalue()
