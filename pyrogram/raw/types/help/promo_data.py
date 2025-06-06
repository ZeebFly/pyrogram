
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


class PromoData(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.PromoData`.

    Details:
        - Layer: ``166``
        - ID: ``8C39793F``

    Parameters:
        expires (``int`` ``32-bit``):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        proxy (``bool``, *optional*):
            N/A

        psa_type (``str``, *optional*):
            N/A

        psa_message (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPromoData
    """

    __slots__: List[str] = ["expires", "peer", "chats", "users", "proxy", "psa_type", "psa_message"]

    ID = 0x8c39793f
    QUALNAME = "types.help.PromoData"

    def __init__(self, *, expires: int, peer: "raw.base.Peer", chats: List["raw.base.Chat"], users: List["raw.base.User"], proxy: Optional[bool] = None, psa_type: Optional[str] = None, psa_message: Optional[str] = None) -> None:
        self.expires = expires  # int
        self.peer = peer  # Peer
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.proxy = proxy  # flags.0?true
        self.psa_type = psa_type  # flags.1?string
        self.psa_message = psa_message  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PromoData":
        
        flags = Int.read(b)
        
        proxy = True if flags & (1 << 0) else False
        expires = Int.read(b)
        
        peer = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        psa_type = String.read(b) if flags & (1 << 1) else None
        psa_message = String.read(b) if flags & (1 << 2) else None
        return PromoData(expires=expires, peer=peer, chats=chats, users=users, proxy=proxy, psa_type=psa_type, psa_message=psa_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.proxy else 0
        flags |= (1 << 1) if self.psa_type is not None else 0
        flags |= (1 << 2) if self.psa_message is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.expires))
        
        b.write(self.peer.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        if self.psa_type is not None:
            b.write(String(self.psa_type))
        
        if self.psa_message is not None:
            b.write(String(self.psa_message))
        
        return b.getvalue()
