
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


class GetAuthorizationForm(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``A929597A``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        scope (``str``):
            N/A

        public_key (``str``):
            N/A

    Returns:
        :obj:`account.AuthorizationForm <pyrogram.raw.base.account.AuthorizationForm>`
    """

    __slots__: List[str] = ["bot_id", "scope", "public_key"]

    ID = 0xa929597a
    QUALNAME = "functions.account.GetAuthorizationForm"

    def __init__(self, *, bot_id: int, scope: str, public_key: str) -> None:
        self.bot_id = bot_id  # long
        self.scope = scope  # string
        self.public_key = public_key  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAuthorizationForm":
        # No flags
        
        bot_id = Long.read(b)
        
        scope = String.read(b)
        
        public_key = String.read(b)
        
        return GetAuthorizationForm(bot_id=bot_id, scope=scope, public_key=public_key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.scope))
        
        b.write(String(self.public_key))
        
        return b.getvalue()
