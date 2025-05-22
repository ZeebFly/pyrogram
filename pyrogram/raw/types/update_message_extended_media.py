
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


class UpdateMessageExtendedMedia(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``166``
        - ID: ``5A73A98C``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        extended_media (:obj:`MessageExtendedMedia <pyrogram.raw.base.MessageExtendedMedia>`):
            N/A

    """

    __slots__: List[str] = ["peer", "msg_id", "extended_media"]

    ID = 0x5a73a98c
    QUALNAME = "types.UpdateMessageExtendedMedia"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, extended_media: "raw.base.MessageExtendedMedia") -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.extended_media = extended_media  # MessageExtendedMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessageExtendedMedia":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        extended_media = TLObject.read(b)
        
        return UpdateMessageExtendedMedia(peer=peer, msg_id=msg_id, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(self.extended_media.write())
        
        return b.getvalue()
