
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


class SetChatAvailableReactions(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``FEB16771``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        available_reactions (:obj:`ChatReactions <pyrogram.raw.base.ChatReactions>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "available_reactions"]

    ID = 0xfeb16771
    QUALNAME = "functions.messages.SetChatAvailableReactions"

    def __init__(self, *, peer: "raw.base.InputPeer", available_reactions: "raw.base.ChatReactions") -> None:
        self.peer = peer  # InputPeer
        self.available_reactions = available_reactions  # ChatReactions

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatAvailableReactions":
        # No flags
        
        peer = TLObject.read(b)
        
        available_reactions = TLObject.read(b)
        
        return SetChatAvailableReactions(peer=peer, available_reactions=available_reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.available_reactions.write())
        
        return b.getvalue()
