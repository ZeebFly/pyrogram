
import pyrogram
from pyrogram import raw


class ExportFolderLink:
    async def export_folder_link(
        self: "pyrogram.Client",
        folder_id: int
    ) -> str:
        """Export link to a user's folder.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            ``str``: On success, a link to the folder as string is returned.

        Example:
            .. code-block:: python

                # Export folder link
                app.export_folder_link(123456789)
        """
        folder = await self.get_folder(folder_id)

        if not folder:
            return

        r = await self.invoke(
            raw.functions.chatlists.ExportChatlistInvite(
                chatlist=raw.types.InputChatlistDialogFilter(
                    filter_id=folder_id
                ),
                title=folder.title,
                peers=[await self.resolve_peer(i.id) for i in folder.pinned_peers] if folder.pinned_peers else []
                + [await self.resolve_peer(i.id) for i in folder.included_peers] if folder.included_peers else []
                + [await self.resolve_peer(i.id) for i in folder.excluded_peers] if folder.excluded_peers else [],
            )
        )

        return r.invite.url
