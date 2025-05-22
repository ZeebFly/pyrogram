
import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class MessageStory(Object):
    """Contains information about a forwarded story.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            Conversation the story belongs to.

        story_id (``int``):
            Unique story identifier.

    """

    def __init__(
        self,
        *,
        chat: "types.Chat",
        story_id: int
    ):
        super().__init__()

        self.chat = chat
        self.story_id = story_id

    @staticmethod
    def _parse(client: "pyrogram.Client", message_story: "raw.types.MessageMediaStory", users, chats) -> "MessageStory":
        peer_id = utils.get_raw_peer_id(message_story.peer)

        if isinstance(message_story.peer, raw.types.PeerChannel):
            chat = types.Chat._parse_channel_chat(client, chats.get(peer_id, None))
        else:
            chat = types.Chat._parse_user_chat(client, users.get(peer_id, None))

        return MessageStory(
            chat=chat,
            story_id=message_story.id
        )
