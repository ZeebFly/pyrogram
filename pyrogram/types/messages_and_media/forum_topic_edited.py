
from pyrogram import raw
from ..object import Object


class ForumTopicEdited(Object):
    """A service message about a forum topic renamed in the chat.


    Parameters:
        title (``String``):
            Name of the topic.

        icon_color (``Integer``):
            Color of the topic icon in RGB format

        icon_custom_emoji_id (``String``, *optional*):
            Unique identifier of the custom emoji shown as the topic icon
    """

    def __init__(
        self, *,
        title: str = None,
        icon_color: int = None,
        icon_emoji_id: str = None
    ):
        super().__init__()

        self.title = title
        self.icon_color = icon_color
        self.icon_emoji_id = icon_emoji_id

    @staticmethod
    def _parse(action: "raw.types.MessageActionTopicEdit") -> "ForumTopicEdited":
        return ForumTopicEdited(
            title=getattr(action, "title", None),
            icon_color=getattr(action, "icon_color", None),
            icon_emoji_id=getattr(action, "icon_emoji_id", None)
        )
