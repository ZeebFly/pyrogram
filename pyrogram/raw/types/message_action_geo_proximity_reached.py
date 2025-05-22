
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


class MessageActionGeoProximityReached(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``98E0D697``

    Parameters:
        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        to_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        distance (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["from_id", "to_id", "distance"]

    ID = 0x98e0d697
    QUALNAME = "types.MessageActionGeoProximityReached"

    def __init__(self, *, from_id: "raw.base.Peer", to_id: "raw.base.Peer", distance: int) -> None:
        self.from_id = from_id  # Peer
        self.to_id = to_id  # Peer
        self.distance = distance  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGeoProximityReached":
        # No flags
        
        from_id = TLObject.read(b)
        
        to_id = TLObject.read(b)
        
        distance = Int.read(b)
        
        return MessageActionGeoProximityReached(from_id=from_id, to_id=to_id, distance=distance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.from_id.write())
        
        b.write(self.to_id.write())
        
        b.write(Int(self.distance))
        
        return b.getvalue()
