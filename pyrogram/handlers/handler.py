
import inspect
from typing import Callable

import pyrogram
from pyrogram.filters import Filter
from pyrogram.types import Update


class Handler:
    def __init__(self, callback: Callable, filters: Filter = None):
        self.callback = callback
        self.filters = filters

    async def check(self, client: "pyrogram.Client", update: Update):
        if callable(self.filters):
            if inspect.iscoroutinefunction(self.filters.__call__):
                return await self.filters(client, update)
            else:
                return await client.loop.run_in_executor(
                    client.executor,
                    self.filters,
                    client, update
                )

        return True
