
from typing import Callable

import pyrogram
from pyrogram.filters import Filter


class OnChosenInlineResult:
    def on_chosen_inline_result(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling chosen inline results.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.ChosenInlineResultHandler`.

        Parameters:
            filters (:obj:`~pyrogram.filters`, *optional*):
                Pass one or more filters to allow only a subset of chosen inline results to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.ChosenInlineResultHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogram.handlers.ChosenInlineResultHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator
