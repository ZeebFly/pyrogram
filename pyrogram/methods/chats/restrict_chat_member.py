
from datetime import datetime
from typing import Union

import pyrogram
from pyrogram import raw, utils
from pyrogram import types


class RestrictChatMember:
    async def restrict_chat_member(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
        permissions: "types.ChatPermissions",
        until_date: datetime = utils.zero_datetime()
    ) -> "types.Chat":
        """Restrict a user in a supergroup.

        You must be an administrator in the supergroup for this to work and must have the appropriate admin rights.
        Pass True for all permissions to lift restrictions from a user.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            permissions (:obj:`~pyrogram.types.ChatPermissions`):
                New user permissions.

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unbanned.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to epoch (ban forever).

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                from datetime import datetime, timedelta
                from pyrogram.types import ChatPermissions

                # Completely restrict chat member (mute) forever
                await app.restrict_chat_member(chat_id, user_id, ChatPermissions())

                # Chat member muted for 24h
                await app.restrict_chat_member(chat_id, user_id, ChatPermissions(),
                    datetime.now() + timedelta(days=1))

                # Chat member can only send text messages
                await app.restrict_chat_member(chat_id, user_id,
                    ChatPermissions(can_send_messages=True))
        """
        r = await self.invoke(
            raw.functions.channels.EditBanned(
                channel=await self.resolve_peer(chat_id),
                participant=await self.resolve_peer(user_id),
                banned_rights=raw.types.ChatBannedRights(
                    until_date=utils.datetime_to_timestamp(until_date),
                    send_messages=not permissions.can_send_messages,
                    send_media=not permissions.can_send_media_messages,
                    send_stickers=not permissions.can_send_other_messages,
                    send_gifs=not permissions.can_send_other_messages,
                    send_games=not permissions.can_send_other_messages,
                    send_inline=not permissions.can_send_other_messages,
                    embed_links=not permissions.can_add_web_page_previews,
                    send_polls=not permissions.can_send_polls,
                    change_info=not permissions.can_change_info,
                    invite_users=not permissions.can_invite_users,
                    pin_messages=not permissions.can_pin_messages,
                    manage_topics=not permissions.can_manage_topics,
                )
            )
        )

        return types.Chat._parse_chat(self, r.chats[0])
