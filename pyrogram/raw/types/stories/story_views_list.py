
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


class StoryViewsList(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.StoryViewsList`.

    Details:
        - Layer: ``166``
        - ID: ``46E9B9EC``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        reactions_count (``int`` ``32-bit``):
            N/A

        views (List of :obj:`StoryView <pyrogram.raw.base.StoryView>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetStoryViewsList
    """

    __slots__: List[str] = ["count", "reactions_count", "views", "users", "next_offset"]

    ID = 0x46e9b9ec
    QUALNAME = "types.stories.StoryViewsList"

    def __init__(self, *, count: int, reactions_count: int, views: List["raw.base.StoryView"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.reactions_count = reactions_count  # int
        self.views = views  # Vector<StoryView>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViewsList":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        reactions_count = Int.read(b)
        
        views = TLObject.read(b)
        
        users = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        return StoryViewsList(count=count, reactions_count=reactions_count, views=views, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Int(self.reactions_count))
        
        b.write(Vector(self.views))
        
        b.write(Vector(self.users))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        return b.getvalue()
