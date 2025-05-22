
import datetime
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram import utils

class UpdateChatNotifications:
    async def update_chat_notifications(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        mute: bool = None,
        mute_until: datetime = None,
        stories_muted: bool = None,
        stories_hide_sender: bool = None,
        show_previews: bool = None
    ) -> "types.Chat":
        """Update the notification settings for the selected chat

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            mute (``bool``, *optional*):
                Pass True if you want to mute chat.

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unmuted. Works only if the mute parameter is set to True. Defaults to forever.

            stories_muted (``bool``, *optional*):
                N/A

            stories_hide_sender (``bool``, *optional*):
                N/A

            show_previews (``bool``, *optional*):
                If the text of the message shall be displayed in notification.

        Returns:
            ``bool``: True on success, False otherwise.

        Example:
            .. code-block:: python

                # Mute a chat permanently
                app.update_chat_notifications(chat_id, mute=True)

                # Mute a chat for 10 minutes
                app.update_chat_notifications(
                    chat_id,
                    mute=True
                    mute_until=datetime.timedelta(minutes=10)
                )

                # Unmute a chat
                app.update_chat_notifications(chat_id, mute=False)
        """
        if not mute_until:
            mute_until = utils.max_datetime() if mute else utils.zero_datetime()

        if isinstance(mute_until, datetime.timedelta):
            mute_until = datetime.datetime.now() + mute_until

        r = await self.invoke(
            raw.functions.account.UpdateNotifySettings(
                peer=raw.types.InputNotifyPeer(peer=await self.resolve_peer(chat_id)),
                settings=raw.types.InputPeerNotifySettings(
                    show_previews=show_previews,
                    silent=mute,
                    mute_until=utils.datetime_to_timestamp(mute_until),
                    stories_muted=stories_muted,
                    stories_hide_sender=stories_hide_sender,
                )
            )
        )

        return r
