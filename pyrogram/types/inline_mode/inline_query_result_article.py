
import pyrogram
from pyrogram import raw
from pyrogram import types

from .inline_query_result import InlineQueryResult


class InlineQueryResultArticle(InlineQueryResult):
    """Link to an article or web page.

    Parameters:
        title (``str``):
            Title for the result.

        input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
            Content of the message to be sent.

        id (``str``, *optional*):
            Unique identifier for this result, 1-64 bytes.
            Defaults to a randomly generated UUID4.

        url (``str``, *optional*):
            URL of the result.

        description (``str``, *optional*):
            Short description of the result.

        reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        thumb_url (``str``, *optional*):
            Url of the thumbnail for the result.

        thumb_width (``int``, *optional*):
            Thumbnail width.

        thumb_height (``int``, *optional*):
            Thumbnail height
    """

    def __init__(
        self,
        title: str,
        input_message_content: "types.InputMessageContent",
        id: str = None,
        url: str = None,
        description: str = None,
        reply_markup: "types.InlineKeyboardMarkup" = None,
        thumb_url: str = None,
        thumb_width: int = 0,
        thumb_height: int = 0
    ):
        super().__init__("article", id, input_message_content, reply_markup)

        self.title = title
        self.url = url
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    async def write(self, client: "pyrogram.Client"):
        return raw.types.InputBotInlineResult(
            id=self.id,
            type=self.type,
            send_message=await self.input_message_content.write(client, self.reply_markup),
            title=self.title,
            description=self.description,
            url=self.url,
            thumb=raw.types.InputWebDocument(
                url=self.thumb_url,
                size=0,
                mime_type="image/jpeg",
                attributes=[
                    raw.types.DocumentAttributeImageSize(
                        w=self.thumb_width,
                        h=self.thumb_height
                    )
                ]
            ) if self.thumb_url else None
        )
