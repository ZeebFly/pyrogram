
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


class GetBoostsList(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``60F67660``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        gifts (``bool``, *optional*):
            N/A

    Returns:
        :obj:`premium.BoostsList <pyrogram.raw.base.premium.BoostsList>`
    """

    __slots__: List[str] = ["peer", "offset", "limit", "gifts"]

    ID = 0x60f67660
    QUALNAME = "functions.premium.GetBoostsList"

    def __init__(self, *, peer: "raw.base.InputPeer", offset: str, limit: int, gifts: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset = offset  # string
        self.limit = limit  # int
        self.gifts = gifts  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBoostsList":
        
        flags = Int.read(b)
        
        gifts = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetBoostsList(peer=peer, offset=offset, limit=limit, gifts=gifts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.gifts else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
