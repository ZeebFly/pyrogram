
from typing import AsyncGenerator, Optional

import pyrogram
from pyrogram import types, raw


class GetFolders:
    async def get_folders(
        self: "pyrogram.Client",
    ) -> Optional[AsyncGenerator["types.Folder", None]]:
        """Get a user's folders with chats sequentially.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Folder` objects.

        Example:
            .. code-block:: python

                # Iterate through all folders
                async for folder in app.get_folders():
                    print(folder.title)
        """
        raw_folders = await self.invoke(raw.functions.messages.GetDialogFilters())
        dialog_peers = []

        for folder in raw_folders:
            if not isinstance(folder, (raw.types.DialogFilter, raw.types.DialogFilterChatlist)):
                continue

            peers = folder.pinned_peers + folder.include_peers + getattr(folder, "exclude_peers", [])
            input_peers = [raw.types.InputDialogPeer(peer=peer) for peer in peers] + [raw.types.InputDialogPeerFolder(folder_id=folder.id)]
            dialog_peers.extend(input_peers)

        r = await self.invoke(raw.functions.messages.GetPeerDialogs(peers=dialog_peers))

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}
        peers = {**users, **chats}

        folders = []

        for folder in raw_folders:
            if not isinstance(folder, (raw.types.DialogFilter, raw.types.DialogFilterChatlist)):
                continue

            folders.append(types.Folder._parse(self, folder, peers))

        if not folders:
            return

        for folder in folders:
            yield folder
