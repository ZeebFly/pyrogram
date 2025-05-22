
from pyrogram import raw
from ..object import Object


class InputReplyToStory(Object):
    """Contains information about a target replied story.

    Parameters:
        user_id (:obj:`~pyrogram.raw.types.InputUser`):
            An InputUser.
            
        story_id (``int``):
            Unique identifier for the target story.
    """

    def __init__(
        self, *,
        user_id: "raw.types.InputUser" = None,
        story_id: int = None
    ):
        super().__init__()

        self.user_id = user_id
        self.story_id = story_id

    def write(self):
        return raw.types.InputReplyToStory(
            user_id=self.user_id,
            story_id=self.story_id
        ).write()
