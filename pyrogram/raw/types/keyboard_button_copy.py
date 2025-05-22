
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class KeyboardButtonCopy(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``195``
        - ID: ``75D2698E``

    Parameters:
        text (``str``):
            N/A

        copy_text (``str``):
            N/A

    """

    __slots__: List[str] = ["text", "copy_text"]

    ID = 0x75d2698e
    QUALNAME = "types.KeyboardButtonCopy"

    def __init__(self, *, text: str, copy_text: str) -> None:
        self.text = text  # string
        self.copy_text = copy_text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonCopy":
        # No flags
        
        text = String.read(b)
        
        copy_text = String.read(b)
        
        return KeyboardButtonCopy(text=text, copy_text=copy_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(String(self.copy_text))
        
        return b.getvalue()
