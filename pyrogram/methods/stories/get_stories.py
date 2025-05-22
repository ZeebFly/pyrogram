
from typing import Union, Iterable

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetStories:
    async def get_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_ids: Union[int, Iterable[int]],
    ) -> "types.Stories":
        """Get stories by id.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For your personal story you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            story_ids (List of ``int`` ``32-bit``):
                Pass a single story identifier or an iterable of story ids (as integers) to get the content of the
                story themselves.

        Returns:
            :obj:`~pyrogram.types.Story` | List of :obj:`~pyrogram.types.Story`: In case *story_ids* was not
            a list, a single story is returned, otherwise a list of stories is returned.

        Example:
            .. code-block:: python

                # Get stories by id
                stories = await app.get_stories_by_id(chat_id, [1, 2, 3])

                for story in stories:
                    print(story)
        """
        is_iterable = not isinstance(story_ids, int)
        ids = list(story_ids) if is_iterable else [story_ids]

        peer = await self.resolve_peer(chat_id)
        r = await self.invoke(
            raw.functions.stories.GetStoriesByID(
                peer=peer,
                id=ids
            )
        )

        stories = []

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for story in r.stories:
            stories.append(
                await types.Story._parse(
                    self,
                    story,
                    users,
                    chats,
                    peer
                )
            )

        return types.List(stories) if is_iterable else stories[0]
