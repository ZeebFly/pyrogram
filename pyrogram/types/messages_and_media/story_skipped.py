
import pyrogram

from datetime import datetime
from pyrogram import raw, types, utils
from pyrogram.errors import PeerIdInvalid
from typing import Union
from ..object import Object
from ..update import Update

class StorySkipped(Object, Update):
    """A skipped story.

    Parameters:
        id (``int``):
            Unique story identifier.

        from_user (:obj:`~pyrogram.types.User`, *optional*):
            Sender of the story.

        sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Sender of the story. If the story is from channel.

        date (:py:obj:`~datetime.datetime`, *optional*):
            Date the story was sent.

        expire_date (:py:obj:`~datetime.datetime`, *optional*):
            Date the story will be expired.

        close_friends (``bool``, *optional*):
           True, if the Story is shared with close_friends only.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        from_user: "types.User" = None,
        sender_chat: "types.Chat" = None,
        date: datetime,
        expire_date: datetime,
        close_friends: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.date = date
        self.expire_date = expire_date
        self.close_friends = close_friends

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        stories: raw.base.StoryItem,
        users: dict,
        chats: dict,
        peer: Union["raw.types.PeerChannel", "raw.types.PeerUser"]
    ) -> "StorySkipped":
        from_user = None
        sender_chat = None

        if isinstance(peer, raw.types.InputPeerSelf):
            r = await client.invoke(raw.functions.users.GetUsers(id=[raw.types.InputPeerSelf()]))
            peer_id = r[0].id
            users.update({i.id: i for i in r})
        elif isinstance(peer, (raw.types.InputPeerUser, raw.types.InputPeerChannel)):
            peer_id = utils.get_input_peer_id(peer)
        else:
            peer_id = utils.get_raw_peer_id(peer)

        if isinstance(peer, (raw.types.PeerUser, raw.types.InputPeerUser)) and peer_id not in users:
            try:
                r = await client.invoke(
                    raw.functions.users.GetUsers(
                        id=[
                            await client.resolve_peer(peer_id)
                        ]
                    )
                )
            except PeerIdInvalid:
                pass
            else:
                users.update({i.id: i for i in r})

        from_user = types.User._parse(client, users.get(peer_id, None))
        sender_chat = types.Chat._parse_channel_chat(client, chats[peer_id]) if not from_user else None

        return StorySkipped(
            id=stories.id,
            from_user=from_user,
            sender_chat=sender_chat,
            date=utils.timestamp_to_datetime(stories.date),
            expire_date=utils.timestamp_to_datetime(stories.expire_date),
            close_friends=stories.close_friends,
            client=client
        )
