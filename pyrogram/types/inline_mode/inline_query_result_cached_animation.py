
from typing import Optional, List

import pyrogram
from pyrogram import raw, types, utils, enums
from .inline_query_result import InlineQueryResult
from ...file_id import FileId


class InlineQueryResultCachedAnimation(InlineQueryResult):
    """A link to an animation file stored on the Telegram servers.

    By default, this animation file will be sent by the user with an optional caption.
    Alternatively, you can use *input_message_content* to send a message with specified content instead of the
    animation.

    Parameters:
        animation_file_id (``str``):
            A valid file identifier for the animation file.

        id (``str``, *optional*):
            Unique identifier for this result, 1-64 bytes.
            Defaults to a randomly generated UUID4.

        title (``str``, *optional*):
            Title for the result.

        caption (``str``, *optional*):
            Caption of the photo to be sent, 0-1024 characters.

        parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
            By default, texts are parsed using both Markdown and HTML styles.
            You can combine both syntaxes together.

        caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
            List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

        reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
            An InlineKeyboardMarkup object.

        input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
            Content of the message to be sent instead of the photo.
    """

    def __init__(
        self,
        animation_file_id: str,
        id: str = None,
        title: str = None,
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        reply_markup: "types.InlineKeyboardMarkup" = None,
        input_message_content: "types.InputMessageContent" = None
    ):
        super().__init__("gif", id, input_message_content, reply_markup)

        self.animation_file_id = animation_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    async def write(self, client: "pyrogram.Client"):
        message, entities = (await utils.parse_text_entities(
            client, self.caption, self.parse_mode, self.caption_entities
        )).values()

        file_id = FileId.decode(self.animation_file_id)

        return raw.types.InputBotInlineResultDocument(
            id=self.id,
            type=self.type,
            title=self.title,
            document=raw.types.InputDocument(
                id=file_id.media_id,
                access_hash=file_id.access_hash,
                file_reference=file_id.file_reference,
            ),
            send_message=(
                await self.input_message_content.write(client, self.reply_markup)
                if self.input_message_content
                else raw.types.InputBotInlineMessageMediaAuto(
                    reply_markup=await self.reply_markup.write(client) if self.reply_markup else None,
                    message=message,
                    entities=entities
                )
            )
        )
