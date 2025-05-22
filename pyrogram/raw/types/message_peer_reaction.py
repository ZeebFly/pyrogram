
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


class MessagePeerReaction(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessagePeerReaction`.

    Details:
        - Layer: ``166``
        - ID: ``8C79B63C``

    Parameters:
        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

        big (``bool``, *optional*):
            N/A

        unread (``bool``, *optional*):
            N/A

        my (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer_id", "date", "reaction", "big", "unread", "my"]

    ID = 0x8c79b63c
    QUALNAME = "types.MessagePeerReaction"

    def __init__(self, *, peer_id: "raw.base.Peer", date: int, reaction: "raw.base.Reaction", big: Optional[bool] = None, unread: Optional[bool] = None, my: Optional[bool] = None) -> None:
        self.peer_id = peer_id  # Peer
        self.date = date  # int
        self.reaction = reaction  # Reaction
        self.big = big  # flags.0?true
        self.unread = unread  # flags.1?true
        self.my = my  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerReaction":
        
        flags = Int.read(b)
        
        big = True if flags & (1 << 0) else False
        unread = True if flags & (1 << 1) else False
        my = True if flags & (1 << 2) else False
        peer_id = TLObject.read(b)
        
        date = Int.read(b)
        
        reaction = TLObject.read(b)
        
        return MessagePeerReaction(peer_id=peer_id, date=date, reaction=reaction, big=big, unread=unread, my=my)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.big else 0
        flags |= (1 << 1) if self.unread else 0
        flags |= (1 << 2) if self.my else 0
        b.write(Int(flags))
        
        b.write(self.peer_id.write())
        
        b.write(Int(self.date))
        
        b.write(self.reaction.write())
        
        return b.getvalue()
