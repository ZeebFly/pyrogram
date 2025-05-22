
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


class KeyboardButtonUserProfile(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``166``
        - ID: ``308660C1``

    Parameters:
        text (``str``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["text", "user_id"]

    ID = 0x308660c1
    QUALNAME = "types.KeyboardButtonUserProfile"

    def __init__(self, *, text: str, user_id: int) -> None:
        self.text = text  # string
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonUserProfile":
        # No flags
        
        text = String.read(b)
        
        user_id = Long.read(b)
        
        return KeyboardButtonUserProfile(text=text, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(Long(self.user_id))
        
        return b.getvalue()
