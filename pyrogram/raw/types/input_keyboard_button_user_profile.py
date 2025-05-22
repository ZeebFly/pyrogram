
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


class InputKeyboardButtonUserProfile(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``166``
        - ID: ``E988037B``

    Parameters:
        text (``str``):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    """

    __slots__: List[str] = ["text", "user_id"]

    ID = 0xe988037b
    QUALNAME = "types.InputKeyboardButtonUserProfile"

    def __init__(self, *, text: str, user_id: "raw.base.InputUser") -> None:
        self.text = text  # string
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUserProfile":
        # No flags
        
        text = String.read(b)
        
        user_id = TLObject.read(b)
        
        return InputKeyboardButtonUserProfile(text=text, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(self.user_id.write())
        
        return b.getvalue()
