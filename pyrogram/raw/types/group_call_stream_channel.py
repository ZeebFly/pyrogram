
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


class GroupCallStreamChannel(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.GroupCallStreamChannel`.

    Details:
        - Layer: ``166``
        - ID: ``80EB48AF``

    Parameters:
        channel (``int`` ``32-bit``):
            N/A

        scale (``int`` ``32-bit``):
            N/A

        last_timestamp_ms (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["channel", "scale", "last_timestamp_ms"]

    ID = 0x80eb48af
    QUALNAME = "types.GroupCallStreamChannel"

    def __init__(self, *, channel: int, scale: int, last_timestamp_ms: int) -> None:
        self.channel = channel  # int
        self.scale = scale  # int
        self.last_timestamp_ms = last_timestamp_ms  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStreamChannel":
        # No flags
        
        channel = Int.read(b)
        
        scale = Int.read(b)
        
        last_timestamp_ms = Long.read(b)
        
        return GroupCallStreamChannel(channel=channel, scale=scale, last_timestamp_ms=last_timestamp_ms)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.channel))
        
        b.write(Int(self.scale))
        
        b.write(Long(self.last_timestamp_ms))
        
        return b.getvalue()
