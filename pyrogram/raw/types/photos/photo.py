
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


class Photo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.photos.Photo`.

    Details:
        - Layer: ``166``
        - ID: ``20212CA8``

    Parameters:
        photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            photos.UpdateProfilePhoto
            photos.UploadProfilePhoto
            photos.UploadContactProfilePhoto
    """

    __slots__: List[str] = ["photo", "users"]

    ID = 0x20212ca8
    QUALNAME = "types.photos.Photo"

    def __init__(self, *, photo: "raw.base.Photo", users: List["raw.base.User"]) -> None:
        self.photo = photo  # Photo
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Photo":
        # No flags
        
        photo = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Photo(photo=photo, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.photo.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
