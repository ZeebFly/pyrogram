
from pyrogram import raw
from ..object import Object


class WebAppData(Object):
    """Contains data sent from a `Web App <https://core.telegram.org/bots/webapps>`_ to the bot.

    Parameters:
        data (``str``):
            The data.

        button_text (``str``):
            Text of the *web_app* keyboard button, from which the Web App was opened.

    """

    def __init__(
        self,
        *,
        data: str,
        button_text: str,
    ):
        super().__init__()

        self.data = data
        self.button_text = button_text

    @staticmethod
    def _parse(action: "raw.types.MessageActionWebViewDataSentMe"):
        return WebAppData(
            data=action.data,
            button_text=action.text
        )
