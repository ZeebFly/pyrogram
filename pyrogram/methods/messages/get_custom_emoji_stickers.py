
from typing import List

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetCustomEmojiStickers:
    async def get_custom_emoji_stickers(
        self: "pyrogram.Client",
        custom_emoji_ids: List[int],
    ) -> List["types.Sticker"]:
        """Get information about custom emoji stickers by their identifiers.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            custom_emoji_ids (List of ``int``):
                List of custom emoji identifiers.
                At most 200 custom emoji identifiers can be specified.

        Returns:
            List of :obj:`~pyrogram.types.Sticker`: On success, a list of sticker objects is returned.
        """
        result = await self.invoke(
            raw.functions.messages.GetCustomEmojiDocuments(
                document_id=custom_emoji_ids
            )
        )

        stickers = []
        for item in result:
            attributes = {type(i): i for i in item.attributes}
            sticker = await types.Sticker._parse(self, item, attributes)
            stickers.append(sticker)

        return pyrogram.types.List(stickers)
