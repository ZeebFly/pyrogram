
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


class Found(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.Found`.

    Details:
        - Layer: ``166``
        - ID: ``B3134D9D``

    Parameters:
        my_results (List of :obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        results (List of :obj:`Peer <pyrogram.raw.base.Peer>`):
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

            contacts.Search
    """

    __slots__: List[str] = ["my_results", "results", "chats", "users"]

    ID = 0xb3134d9d
    QUALNAME = "types.contacts.Found"

    def __init__(self, *, my_results: List["raw.base.Peer"], results: List["raw.base.Peer"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.my_results = my_results  # Vector<Peer>
        self.results = results  # Vector<Peer>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Found":
        # No flags
        
        my_results = TLObject.read(b)
        
        results = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Found(my_results=my_results, results=results, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.my_results))
        
        b.write(Vector(self.results))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
