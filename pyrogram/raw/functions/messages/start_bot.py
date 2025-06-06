
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


class StartBot(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``E6DF7378``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        start_param (``str``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["bot", "peer", "random_id", "start_param"]

    ID = 0xe6df7378
    QUALNAME = "functions.messages.StartBot"

    def __init__(self, *, bot: "raw.base.InputUser", peer: "raw.base.InputPeer", random_id: int, start_param: str) -> None:
        self.bot = bot  # InputUser
        self.peer = peer  # InputPeer
        self.random_id = random_id  # long
        self.start_param = start_param  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartBot":
        # No flags
        
        bot = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        random_id = Long.read(b)
        
        start_param = String.read(b)
        
        return StartBot(bot=bot, peer=peer, random_id=random_id, start_param=start_param)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(self.peer.write())
        
        b.write(Long(self.random_id))
        
        b.write(String(self.start_param))
        
        return b.getvalue()
