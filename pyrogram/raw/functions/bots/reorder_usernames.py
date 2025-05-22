
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


class ReorderUsernames(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``9709B1C2``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        order (List of ``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot", "order"]

    ID = 0x9709b1c2
    QUALNAME = "functions.bots.ReorderUsernames"

    def __init__(self, *, bot: "raw.base.InputUser", order: List[str]) -> None:
        self.bot = bot  # InputUser
        self.order = order  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderUsernames":
        # No flags
        
        bot = TLObject.read(b)
        
        order = TLObject.read(b, String)
        
        return ReorderUsernames(bot=bot, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Vector(self.order, String))
        
        return b.getvalue()
