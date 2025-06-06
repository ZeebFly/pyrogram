
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


class KeyboardButtonRequestPeer(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``166``
        - ID: ``D0B468C``

    Parameters:
        text (``str``):
            N/A

        button_id (``int`` ``32-bit``):
            N/A

        peer_type (:obj:`RequestPeerType <pyrogram.raw.base.RequestPeerType>`):
            N/A

    """

    __slots__: List[str] = ["text", "button_id", "peer_type"]

    ID = 0xd0b468c
    QUALNAME = "types.KeyboardButtonRequestPeer"

    def __init__(self, *, text: str, button_id: int, peer_type: "raw.base.RequestPeerType") -> None:
        self.text = text  # string
        self.button_id = button_id  # int
        self.peer_type = peer_type  # RequestPeerType

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRequestPeer":
        # No flags
        
        text = String.read(b)
        
        button_id = Int.read(b)
        
        peer_type = TLObject.read(b)
        
        return KeyboardButtonRequestPeer(text=text, button_id=button_id, peer_type=peer_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(Int(self.button_id))
        
        b.write(self.peer_type.write())
        
        return b.getvalue()
