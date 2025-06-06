
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


class ChatAdminsWithInvites(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ChatAdminsWithInvites`.

    Details:
        - Layer: ``166``
        - ID: ``B69B72D7``

    Parameters:
        admins (List of :obj:`ChatAdminWithInvites <pyrogram.raw.base.ChatAdminWithInvites>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAdminsWithInvites
    """

    __slots__: List[str] = ["admins", "users"]

    ID = 0xb69b72d7
    QUALNAME = "types.messages.ChatAdminsWithInvites"

    def __init__(self, *, admins: List["raw.base.ChatAdminWithInvites"], users: List["raw.base.User"]) -> None:
        self.admins = admins  # Vector<ChatAdminWithInvites>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminsWithInvites":
        # No flags
        
        admins = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatAdminsWithInvites(admins=admins, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.admins))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
