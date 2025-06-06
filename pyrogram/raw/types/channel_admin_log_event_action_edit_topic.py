
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


class ChannelAdminLogEventActionEditTopic(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``166``
        - ID: ``F06FE208``

    Parameters:
        prev_topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            N/A

        new_topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            N/A

    """

    __slots__: List[str] = ["prev_topic", "new_topic"]

    ID = 0xf06fe208
    QUALNAME = "types.ChannelAdminLogEventActionEditTopic"

    def __init__(self, *, prev_topic: "raw.base.ForumTopic", new_topic: "raw.base.ForumTopic") -> None:
        self.prev_topic = prev_topic  # ForumTopic
        self.new_topic = new_topic  # ForumTopic

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionEditTopic":
        # No flags
        
        prev_topic = TLObject.read(b)
        
        new_topic = TLObject.read(b)
        
        return ChannelAdminLogEventActionEditTopic(prev_topic=prev_topic, new_topic=new_topic)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_topic.write())
        
        b.write(self.new_topic.write())
        
        return b.getvalue()
