
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


class MessageMediaPoll(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``166``
        - ID: ``4BD6E798``

    Parameters:
        poll (:obj:`Poll <pyrogram.raw.base.Poll>`):
            N/A

        results (:obj:`PollResults <pyrogram.raw.base.PollResults>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPagePreview
            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["poll", "results"]

    ID = 0x4bd6e798
    QUALNAME = "types.MessageMediaPoll"

    def __init__(self, *, poll: "raw.base.Poll", results: "raw.base.PollResults") -> None:
        self.poll = poll  # Poll
        self.results = results  # PollResults

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaPoll":
        # No flags
        
        poll = TLObject.read(b)
        
        results = TLObject.read(b)
        
        return MessageMediaPoll(poll=poll, results=results)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.poll.write())
        
        b.write(self.results.write())
        
        return b.getvalue()
