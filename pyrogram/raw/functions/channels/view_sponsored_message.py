
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


class ViewSponsoredMessage(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``BEAEDB94``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        random_id (``bytes``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "random_id"]

    ID = 0xbeaedb94
    QUALNAME = "functions.channels.ViewSponsoredMessage"

    def __init__(self, *, channel: "raw.base.InputChannel", random_id: bytes) -> None:
        self.channel = channel  # InputChannel
        self.random_id = random_id  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ViewSponsoredMessage":
        # No flags
        
        channel = TLObject.read(b)
        
        random_id = Bytes.read(b)
        
        return ViewSponsoredMessage(channel=channel, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Bytes(self.random_id))
        
        return b.getvalue()
