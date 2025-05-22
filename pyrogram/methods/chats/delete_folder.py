
import pyrogram
from pyrogram import raw


class DeleteFolder:
    async def delete_folder(
        self: "pyrogram.Client",
        folder_id: int
    ) -> bool:
        """Delete a user's folder.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            ``bool``: True, on success.

        Example:
            .. code-block:: python

                # Delete folder
                app.delete_folder(123456789)
        """
        r = await self.invoke(
            raw.functions.messages.UpdateDialogFilter(
                id=folder_id
            )
        )

        return r
