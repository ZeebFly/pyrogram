
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class StopPoll:
    async def stop_poll(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        reply_markup: "types.InlineKeyboardMarkup" = None
    ) -> "types.Poll":
        """Stop a poll which was sent by you.

        Stopped polls can't be reopened and nobody will be able to vote in it anymore.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Identifier of the original message with the poll.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~pyrogram.types.Poll`: On success, the stopped poll with the final results is returned.

        Example:
            .. code-block:: python

                await app.stop_poll(chat_id, message_id)
        """
        poll = (await self.get_messages(chat_id, message_id)).poll

        r = await self.invoke(
            raw.functions.messages.EditMessage(
                peer=await self.resolve_peer(chat_id),
                id=message_id,
                media=raw.types.InputMediaPoll(
                    poll=raw.types.Poll(
                        id=int(poll.id),
                        closed=True,
                        question="",
                        answers=[]
                    )
                ),
                reply_markup=await reply_markup.write(self) if reply_markup else None
            )
        )

        return types.Poll._parse(self, r.updates[0])
