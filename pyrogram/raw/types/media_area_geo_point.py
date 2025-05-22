
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


class MediaAreaGeoPoint(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``166``
        - ID: ``DF8B3B22``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            N/A

    """

    __slots__: List[str] = ["coordinates", "geo"]

    ID = 0xdf8b3b22
    QUALNAME = "types.MediaAreaGeoPoint"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", geo: "raw.base.GeoPoint") -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.geo = geo  # GeoPoint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaGeoPoint":
        # No flags
        
        coordinates = TLObject.read(b)
        
        geo = TLObject.read(b)
        
        return MediaAreaGeoPoint(coordinates=coordinates, geo=geo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(self.geo.write())
        
        return b.getvalue()
