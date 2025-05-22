
from pyrogram import raw, types
from typing import List
from ..object import Object

class StoryViews(Object):
    """Contains information about a story viewers.

    Parameters:
        views_count (``int`` ``32-bit``):
            Views count.

        has_viewers (``bool``, *optional*):
            Has viewers.

        forwards_count (``int`` ``32-bit``, *optional*):
            Forwards count.

        reactions (List of :obj:`~pyrogram.types.Reaction`, *optional*):
            Reactions list.

        reactions_count (``int`` ``32-bit``, *optional*):
            Reactions count.

        recent_viewers (List of ``int`` ``64-bit``, *optional*):
            Viewers list.
    """

    def __init__(
            self, *,
            views_count: int,
            has_viewers: bool = None,
            forwards_count: int = None,
            reactions: List["types.Reaction"] = None,
            reactions_count: int = None,
            recent_viewers: List[int] = None
    ):
        super().__init__()

        self.views_count = views_count
        self.has_viewers = has_viewers
        self.forwards_count = forwards_count
        self.reactions = reactions
        self.reactions_count = reactions_count
        self.recent_viewers = recent_viewers

    @staticmethod
    def _parse(client, storyviews: "raw.types.StoryViews") -> "StoryViews":
        return StoryViews(
            views_count=getattr(storyviews, "views_count", None),
            has_viewers=getattr(storyviews, "has_viewers", None),
            forwards_count=getattr(storyviews, "forwards_count", None),
            reactions=[
                types.Reaction._parse_count(client, reaction)
                for reaction in getattr(storyviews, "reactions", [])
            ] or None,
            recent_viewers=getattr(storyviews, "recent_viewers", None) or None,
        )
