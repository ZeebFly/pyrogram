
from typing import List

import pyrogram
from pyrogram import raw, types


class GetBotCommands:
    async def get_bot_commands(
        self: "pyrogram.Client",
        scope: "types.BotCommandScope" = types.BotCommandScopeDefault(),
        language_code: str = "",
    ) -> List["types.BotCommand"]:
        """Get the current list of the bot's commands for the given scope and user language.
        Returns Array of BotCommand on success. If commands aren't set, an empty list is returned.

        The commands passed will overwrite any command set previously.
        This method can be used by the own bot only.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            scope (:obj:`~pyrogram.types.BotCommandScope`, *optional*):
                An object describing the scope of users for which the commands are relevant.
                Defaults to :obj:`~pyrogram.types.BotCommandScopeDefault`.

            language_code (``str``, *optional*):
                A two-letter ISO 639-1 language code.
                If empty, commands will be applied to all users from the given scope, for whose language there are no
                dedicated commands.

        Returns:
            List of :obj:`~pyrogram.types.BotCommand`: On success, the list of bot commands is returned.

        Example:
            .. code-block:: python

                # Get commands
                commands = await app.get_bot_commands()
                print(commands)
        """

        r = await self.invoke(
            raw.functions.bots.GetBotCommands(
                scope=await scope.write(self),
                lang_code=language_code,
            )
        )

        return types.List(types.BotCommand.read(c) for c in r)
