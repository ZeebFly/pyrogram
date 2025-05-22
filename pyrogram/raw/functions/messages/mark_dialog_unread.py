
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


class MarkDialogUnread(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``C286D98F``

    Parameters:
        peer (:obj:`InputDialogPeer <pyrogram.raw.base.InputDialogPeer>`):
            N/A

        unread (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "unread"]

    ID = 0xc286d98f
    QUALNAME = "functions.messages.MarkDialogUnread"

    def __init__(self, *, peer: "raw.base.InputDialogPeer", unread: Optional[bool] = None) -> None:
        self.peer = peer  # InputDialogPeer
        self.unread = unread  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MarkDialogUnread":
        
        flags = Int.read(b)
        
        unread = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return MarkDialogUnread(peer=peer, unread=unread)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unread else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()
