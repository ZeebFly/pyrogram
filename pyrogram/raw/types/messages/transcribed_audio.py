
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


class TranscribedAudio(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.TranscribedAudio`.

    Details:
        - Layer: ``166``
        - ID: ``93752C52``

    Parameters:
        transcription_id (``int`` ``64-bit``):
            N/A

        text (``str``):
            N/A

        pending (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.TranscribeAudio
    """

    __slots__: List[str] = ["transcription_id", "text", "pending"]

    ID = 0x93752c52
    QUALNAME = "types.messages.TranscribedAudio"

    def __init__(self, *, transcription_id: int, text: str, pending: Optional[bool] = None) -> None:
        self.transcription_id = transcription_id  # long
        self.text = text  # string
        self.pending = pending  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranscribedAudio":
        
        flags = Int.read(b)
        
        pending = True if flags & (1 << 0) else False
        transcription_id = Long.read(b)
        
        text = String.read(b)
        
        return TranscribedAudio(transcription_id=transcription_id, text=text, pending=pending)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pending else 0
        b.write(Int(flags))
        
        b.write(Long(self.transcription_id))
        
        b.write(String(self.text))
        
        return b.getvalue()
