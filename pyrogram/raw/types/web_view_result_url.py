
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


class WebViewResultUrl(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebViewResult`.

    Details:
        - Layer: ``166``
        - ID: ``C14557C``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        url (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestWebView
    """

    __slots__: List[str] = ["query_id", "url"]

    ID = 0xc14557c
    QUALNAME = "types.WebViewResultUrl"

    def __init__(self, *, query_id: int, url: str) -> None:
        self.query_id = query_id  # long
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebViewResultUrl":
        # No flags
        
        query_id = Long.read(b)
        
        url = String.read(b)
        
        return WebViewResultUrl(query_id=query_id, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(String(self.url))
        
        return b.getvalue()
