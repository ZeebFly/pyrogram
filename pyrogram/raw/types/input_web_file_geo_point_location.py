
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


class InputWebFileGeoPointLocation(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``166``
        - ID: ``9F2221C9``

    Parameters:
        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        w (``int`` ``32-bit``):
            N/A

        h (``int`` ``32-bit``):
            N/A

        zoom (``int`` ``32-bit``):
            N/A

        scale (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["geo_point", "access_hash", "w", "h", "zoom", "scale"]

    ID = 0x9f2221c9
    QUALNAME = "types.InputWebFileGeoPointLocation"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", access_hash: int, w: int, h: int, zoom: int, scale: int) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.access_hash = access_hash  # long
        self.w = w  # int
        self.h = h  # int
        self.zoom = zoom  # int
        self.scale = scale  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileGeoPointLocation":
        # No flags
        
        geo_point = TLObject.read(b)
        
        access_hash = Long.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        zoom = Int.read(b)
        
        scale = Int.read(b)
        
        return InputWebFileGeoPointLocation(geo_point=geo_point, access_hash=access_hash, w=w, h=h, zoom=zoom, scale=scale)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.geo_point.write())
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        b.write(Int(self.zoom))
        
        b.write(Int(self.scale))
        
        return b.getvalue()
