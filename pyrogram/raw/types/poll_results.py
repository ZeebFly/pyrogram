
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


class PollResults(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PollResults`.

    Details:
        - Layer: ``166``
        - ID: ``7ADF2420``

    Parameters:
        min (``bool``, *optional*):
            N/A

        results (List of :obj:`PollAnswerVoters <pyrogram.raw.base.PollAnswerVoters>`, *optional*):
            N/A

        total_voters (``int`` ``32-bit``, *optional*):
            N/A

        recent_voters (List of :obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        solution (``str``, *optional*):
            N/A

        solution_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["min", "results", "total_voters", "recent_voters", "solution", "solution_entities"]

    ID = 0x7adf2420
    QUALNAME = "types.PollResults"

    def __init__(self, *, min: Optional[bool] = None, results: Optional[List["raw.base.PollAnswerVoters"]] = None, total_voters: Optional[int] = None, recent_voters: Optional[List["raw.base.Peer"]] = None, solution: Optional[str] = None, solution_entities: Optional[List["raw.base.MessageEntity"]] = None) -> None:
        self.min = min  # flags.0?true
        self.results = results  # flags.1?Vector<PollAnswerVoters>
        self.total_voters = total_voters  # flags.2?int
        self.recent_voters = recent_voters  # flags.3?Vector<Peer>
        self.solution = solution  # flags.4?string
        self.solution_entities = solution_entities  # flags.4?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollResults":
        
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        results = TLObject.read(b) if flags & (1 << 1) else []
        
        total_voters = Int.read(b) if flags & (1 << 2) else None
        recent_voters = TLObject.read(b) if flags & (1 << 3) else []
        
        solution = String.read(b) if flags & (1 << 4) else None
        solution_entities = TLObject.read(b) if flags & (1 << 4) else []
        
        return PollResults(min=min, results=results, total_voters=total_voters, recent_voters=recent_voters, solution=solution, solution_entities=solution_entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min else 0
        flags |= (1 << 1) if self.results else 0
        flags |= (1 << 2) if self.total_voters is not None else 0
        flags |= (1 << 3) if self.recent_voters else 0
        flags |= (1 << 4) if self.solution is not None else 0
        flags |= (1 << 4) if self.solution_entities else 0
        b.write(Int(flags))
        
        if self.results is not None:
            b.write(Vector(self.results))
        
        if self.total_voters is not None:
            b.write(Int(self.total_voters))
        
        if self.recent_voters is not None:
            b.write(Vector(self.recent_voters))
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        return b.getvalue()
