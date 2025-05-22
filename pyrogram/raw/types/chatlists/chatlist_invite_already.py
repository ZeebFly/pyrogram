
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


class ChatlistInviteAlready(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.chatlists.ChatlistInvite`.

    Details:
        - Layer: ``166``
        - ID: ``FA87F659``

    Parameters:
        filter_id (``int`` ``32-bit``):
            N/A

        missing_peers (List of :obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        already_peers (List of :obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.CheckChatlistInvite
    """

    __slots__: List[str] = ["filter_id", "missing_peers", "already_peers", "chats", "users"]

    ID = 0xfa87f659
    QUALNAME = "types.chatlists.ChatlistInviteAlready"

    def __init__(self, *, filter_id: int, missing_peers: List["raw.base.Peer"], already_peers: List["raw.base.Peer"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.filter_id = filter_id  # int
        self.missing_peers = missing_peers  # Vector<Peer>
        self.already_peers = already_peers  # Vector<Peer>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatlistInviteAlready":
        # No flags
        
        filter_id = Int.read(b)
        
        missing_peers = TLObject.read(b)
        
        already_peers = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatlistInviteAlready(filter_id=filter_id, missing_peers=missing_peers, already_peers=already_peers, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.filter_id))
        
        b.write(Vector(self.missing_peers))
        
        b.write(Vector(self.already_peers))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
