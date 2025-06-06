
from typing import Union

import pyrogram
from pyrogram import raw


class RequestCallbackAnswer:
    async def request_callback_answer(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        callback_data: Union[str, bytes],
        timeout: int = 10
    ):
        """Request a callback answer from bots.
        This is the equivalent of clicking an inline button containing callback data.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                The message id the inline keyboard is attached on.

            callback_data (``str`` | ``bytes``):
                Callback data associated with the inline button you want to get the answer from.

            timeout (``int``, *optional*):
                Timeout in seconds.

        Returns:
            The answer containing info useful for clients to display a notification at the top of the chat screen
            or as an alert.

        Raises:
            TimeoutError: In case the bot fails to answer within 10 seconds.

        Example:
            .. code-block:: python

                await app.request_callback_answer(chat_id, message_id, "callback_data")
        """

        # Telegram only wants bytes, but we are allowed to pass strings too.
        data = bytes(callback_data, "utf-8") if isinstance(callback_data, str) else callback_data

        return await self.invoke(
            raw.functions.messages.GetBotCallbackAnswer(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                data=data
            ),
            retries=0,
            timeout=timeout
        )
