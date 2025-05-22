
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


class MessageActionChatMigrateTo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``E1037F92``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["channel_id"]

    ID = 0xe1037f92
    QUALNAME = "types.MessageActionChatMigrateTo"

    def __init__(self, *, channel_id: int) -> None:
        self.channel_id = channel_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatMigrateTo":
        # No flags
        
        channel_id = Long.read(b)
        
        return MessageActionChatMigrateTo(channel_id=channel_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        return b.getvalue()
