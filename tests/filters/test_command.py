#ZeebSupport
import pytest

from pyrogram import filters
from tests.filters import Client, Message

c = Client()


@pytest.mark.asyncio
async def test_single():
    f = filters.command("start")

    m = Message("/start")
    assert await f(c, m)


@pytest.mark.asyncio
async def test_multiple():
    f = filters.command(["start", "help"])

    m = Message("/start")
    assert await f(c, m)

    m = Message("/help")
    assert await f(c, m)

    m = Message("/settings")
    assert not await f(c, m)


@pytest.mark.asyncio
async def test_prefixes():
    f = filters.command("start", prefixes=list(".!#"))

    m = Message(".start")
    assert await f(c, m)

    m = Message("!start")
    assert await f(c, m)

    m = Message("#start")
    assert await f(c, m)

    m = Message("/start")
    assert not await f(c, m)


@pytest.mark.asyncio
async def test_case_sensitive():
    f = filters.command("start", case_sensitive=True)

    m = Message("/start")
    assert await f(c, m)

    m = Message("/StArT")
    assert not await f(c, m)


@pytest.mark.asyncio
async def test_case_insensitive():
    f = filters.command("start", case_sensitive=False)

    m = Message("/start")
    assert await f(c, m)

    m = Message("/StArT")
    assert await f(c, m)


@pytest.mark.asyncio
async def test_with_mention():
    f = filters.command("start")

    m = Message("/start@username")
    assert await f(c, m)

    m = Message("/start@UserName")
    assert await f(c, m)

    m = Message("/start@another")
    assert not await f(c, m)


@pytest.mark.asyncio
async def test_with_args():
    f = filters.command("start")

    m = Message("/start")
    await f(c, m)
    assert m.command == ["start"]

    m = Message("/StArT")
    await f(c, m)
    assert m.command == ["start"]

    m = Message("/start@username")
    await f(c, m)
    assert m.command == ["start"]

    m = Message("/start a b c")
    await f(c, m)
    assert m.command == ["start"] + list("abc")

    m = Message('/start@username a b c')
    await f(c, m)
    assert m.command == ["start"] + list("abc")

    m = Message("/start 'a b' c")
    await f(c, m)
    assert m.command == ["start", "a b", "c"]

    m = Message('/start     a     b     "c     d"')
    await f(c, m)
    assert m.command == ["start"] + list("ab") + ["c     d"]


@pytest.mark.asyncio
async def test_caption():
    f = filters.command("start")

    m = Message(caption="/start")
    assert await f(c, m)


@pytest.mark.asyncio
async def test_no_text():
    f = filters.command("start")

    m = Message()
    assert not await f(c, m)
