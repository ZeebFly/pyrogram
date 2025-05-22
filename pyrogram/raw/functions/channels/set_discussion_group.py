
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


class SetDiscussionGroup(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``40582BB2``

    Parameters:
        broadcast (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        group (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["broadcast", "group"]

    ID = 0x40582bb2
    QUALNAME = "functions.channels.SetDiscussionGroup"

    def __init__(self, *, broadcast: "raw.base.InputChannel", group: "raw.base.InputChannel") -> None:
        self.broadcast = broadcast  # InputChannel
        self.group = group  # InputChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetDiscussionGroup":
        # No flags
        
        broadcast = TLObject.read(b)
        
        group = TLObject.read(b)
        
        return SetDiscussionGroup(broadcast=broadcast, group=group)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.broadcast.write())
        
        b.write(self.group.write())
        
        return b.getvalue()
