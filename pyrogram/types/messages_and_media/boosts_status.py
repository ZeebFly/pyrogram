
from typing import List

from pyrogram import raw, types
from ..object import Object


class BoostsStatus(Object):
    """Contains information about boost.

    Parameters:
        level (``int``):
            Level of channel.

        current_level_boosts (``int``):
            Number of boosts required for the current level.

        boosts (``int``):
            Total number of boosts.

        boost_url (``str``):
            Link that can be used to give a boost to a channel.

        my_boost (``bool``, *optional*):
            True, if you boost this channel.

        gift_boosts (``int``, *optional*):
            N/A

        next_level_boosts (``int``, *optional*):
            Number of boosts at which the next level will be reached.

        my_boost_slots (List of ``int``, *optional*):
            Boost slots that are given to the channel.
    """

    def __init__(
        self,
        *,
        level: int,
        current_level_boosts: int,
        boosts: int,
        boost_url: str,
        my_boost: bool = None,
        gift_boosts: int = None,
        next_level_boosts: int = None,
        my_boost_slots: List[int] = None
    ):
        super().__init__()

        self.level = level
        self.current_level_boosts = current_level_boosts
        self.boosts = boosts
        self.boost_url = boost_url
        self.my_boost = my_boost
        self.gift_boosts = gift_boosts
        self.next_level_boosts = next_level_boosts
        self.my_boost_slots = my_boost_slots

    @staticmethod
    def _parse(boosts_status: "raw.types.premium.BoostsStatus") -> "BoostsStatus":
        return BoostsStatus(
            level=boosts_status.level,
            current_level_boosts=boosts_status.current_level_boosts,
            boosts=boosts_status.boosts,
            boost_url=boosts_status.boost_url,
            my_boost=getattr(boosts_status, "my_boost", None),
            gift_boosts=getattr(boosts_status, "gift_boosts", None),
            next_level_boosts=getattr(boosts_status, "next_level_boosts", None),
            my_boost_slots=types.List(boosts_status.my_boost_slots) or None,
        )
