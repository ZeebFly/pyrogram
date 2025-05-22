
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


class DeleteTopicHistory(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``34435F2D``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        top_msg_id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.AffectedHistory <pyrogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["channel", "top_msg_id"]

    ID = 0x34435f2d
    QUALNAME = "functions.channels.DeleteTopicHistory"

    def __init__(self, *, channel: "raw.base.InputChannel", top_msg_id: int) -> None:
        self.channel = channel  # InputChannel
        self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteTopicHistory":
        # No flags
        
        channel = TLObject.read(b)
        
        top_msg_id = Int.read(b)
        
        return DeleteTopicHistory(channel=channel, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.top_msg_id))
        
        return b.getvalue()
