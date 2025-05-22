
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


class PhoneCallProtocol(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhoneCallProtocol`.

    Details:
        - Layer: ``166``
        - ID: ``FC878FC8``

    Parameters:
        min_layer (``int`` ``32-bit``):
            N/A

        max_layer (``int`` ``32-bit``):
            N/A

        library_versions (List of ``str``):
            N/A

        udp_p2p (``bool``, *optional*):
            N/A

        udp_reflector (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["min_layer", "max_layer", "library_versions", "udp_p2p", "udp_reflector"]

    ID = 0xfc878fc8
    QUALNAME = "types.PhoneCallProtocol"

    def __init__(self, *, min_layer: int, max_layer: int, library_versions: List[str], udp_p2p: Optional[bool] = None, udp_reflector: Optional[bool] = None) -> None:
        self.min_layer = min_layer  # int
        self.max_layer = max_layer  # int
        self.library_versions = library_versions  # Vector<string>
        self.udp_p2p = udp_p2p  # flags.0?true
        self.udp_reflector = udp_reflector  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallProtocol":
        
        flags = Int.read(b)
        
        udp_p2p = True if flags & (1 << 0) else False
        udp_reflector = True if flags & (1 << 1) else False
        min_layer = Int.read(b)
        
        max_layer = Int.read(b)
        
        library_versions = TLObject.read(b, String)
        
        return PhoneCallProtocol(min_layer=min_layer, max_layer=max_layer, library_versions=library_versions, udp_p2p=udp_p2p, udp_reflector=udp_reflector)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.udp_p2p else 0
        flags |= (1 << 1) if self.udp_reflector else 0
        b.write(Int(flags))
        
        b.write(Int(self.min_layer))
        
        b.write(Int(self.max_layer))
        
        b.write(Vector(self.library_versions, String))
        
        return b.getvalue()
