
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


class ReorderPinnedForumTopics(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``2950A18F``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        order (List of ``int`` ``32-bit``):
            N/A

        force (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "order", "force"]

    ID = 0x2950a18f
    QUALNAME = "functions.channels.ReorderPinnedForumTopics"

    def __init__(self, *, channel: "raw.base.InputChannel", order: List[int], force: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.order = order  # Vector<int>
        self.force = force  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderPinnedForumTopics":
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        channel = TLObject.read(b)
        
        order = TLObject.read(b, Int)
        
        return ReorderPinnedForumTopics(channel=channel, order=order, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Vector(self.order, Int))
        
        return b.getvalue()
