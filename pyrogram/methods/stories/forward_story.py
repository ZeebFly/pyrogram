
from datetime import datetime
from typing import Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram import utils

class ForwardStory:
    async def forward_story(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        story_id: int,
        disable_notification: bool = None,
        message_thread_id: int = None,
        schedule_date: datetime = None,
    ) -> Optional["types.Message"]:
        """Send story.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            from_chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            story_id (``int``):
                Unique identifier of story.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.
                for forum supergroups only.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent stoty message is returned.

        Example:
            .. code-block:: python

                # Send your story to chat_id
                await app.forward_story(chat_id, "me", 1)
        """
        r = await self.invoke(
            raw.functions.messages.SendMedia(
                peer=await self.resolve_peer(chat_id),
                media=raw.types.InputMediaStory(
                    peer=await self.resolve_peer(from_chat_id),
                    id=story_id
                ),
                silent=disable_notification or None,
                random_id=self.rnd_id(),
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                message="",
                reply_to=utils.get_reply_to(
                    message_thread_id=message_thread_id
                ),
            )
        )

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                                raw.types.UpdateNewChannelMessage,
                                raw.types.UpdateNewScheduledMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage)
                )
