
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


class Stories(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.Stories`.

    Details:
        - Layer: ``166``
        - ID: ``5DD8C3C8``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        stories (List of :obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetPinnedStories
            stories.GetStoriesArchive
            stories.GetStoriesByID
    """

    __slots__: List[str] = ["count", "stories", "chats", "users"]

    ID = 0x5dd8c3c8
    QUALNAME = "types.stories.Stories"

    def __init__(self, *, count: int, stories: List["raw.base.StoryItem"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.count = count  # int
        self.stories = stories  # Vector<StoryItem>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Stories":
        # No flags
        
        count = Int.read(b)
        
        stories = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Stories(count=count, stories=stories, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.stories))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
