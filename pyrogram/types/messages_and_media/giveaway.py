
from datetime import datetime
from typing import List

import pyrogram
from pyrogram import raw, utils
from pyrogram import types
from ..object import Object


class Giveaway(Object):
    """An giveaway.

    Parameters:
        chats (List of :obj:`~pyrogram.types.Chat`):
            Get the list of channels you need to subscribe to.

        quantity (``int``):
            Number of subscriptions.

        months (``int``):
            Number of months for which a subscription is given.

        until_date (:py:obj:`~datetime.datetime`):
            Date when the giveaway will end.

        only_new_subscribers (``bool``):
            True if the giveaway is for new subscribers only.

        only_for_countries (List of ``str`` , *optional*):
            Countries for which the giveaway is available in iso2 format.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        chats: List["types.Chat"] = None,
        quantity: int = None,
        months: int = None,
        until_date: datetime = None,
        only_new_subscribers: bool = None,
        only_for_countries: List[str] = None

    ):
        super().__init__(client)

        self.chats = chats
        self.quantity = quantity
        self.months = months
        self.until_date = until_date
        self.only_new_subscribers = only_new_subscribers
        self.only_for_countries = only_for_countries

    @staticmethod
    def _parse(
        client,
        giveaway: "raw.types.MessageMediaGiveaway",
        chats: dict
    ) -> "Giveaway":
        return Giveaway(
            chats=types.List(types.Chat._parse_channel_chat(client, chats.get(i)) for i in giveaway.channels),
            quantity=giveaway.quantity,
            months=giveaway.months,
            until_date=utils.timestamp_to_datetime(giveaway.until_date),
            only_new_subscribers=giveaway.only_new_subscribers,
            only_for_countries=types.List(giveaway.countries_iso2) or None,
            client=client
        )
