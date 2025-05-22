
from typing import Optional

import pyrogram
from pyrogram import types


class GetFolder:
    async def get_folder(
        self: "pyrogram.Client",
        folder_id: int
    ) -> Optional["types.Folder"]:
        """Get a user's folder by id.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            :obj:`~pyrogram.types.Folder`: On success, the user's folder is returned.

        Example:
            .. code-block:: python

                # Get folder by id
                await app.get_folder(123456789)
        """
        async for folder in self.get_folders():
            if folder.id == folder_id:
                return folder
