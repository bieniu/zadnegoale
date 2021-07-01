"""Tests for zadnegoale package."""
import json
from datetime import date
from unittest.mock import Mock, patch

import aiohttp
import pytest
from aioresponses import aioresponses

from zadnegoale import ApiError, InvalidRegionError, ZadnegoAle

VALID_REGION = 3
INVALID_REGION = 13
TEST_DATE = date(2021, 1, 1)


@pytest.mark.asyncio
async def test_dusts_and_alerts():
    """Test with valid dusts and alerts data."""
    with open("tests/fixtures/dusts.json") as file:
        dusts = json.load(file)
    with open("tests/fixtures/alerts.json") as file:
        alerts = json.load(file)

    session = aiohttp.ClientSession()

    with aioresponses() as session_mock, patch(
        "zadnegoale.date", today=Mock(return_value=TEST_DATE)
    ):
        session_mock.get(
            f"http://api.zadnegoale.pl/dusts/public/date/20210101/region/{VALID_REGION}",
            payload=dusts,
        )
        session_mock.get(
            f"http://api.zadnegoale.pl/alerts/public/date/20210101/region/{VALID_REGION}",
            payload=alerts,
        )

        zadnegoale = ZadnegoAle(session, VALID_REGION, debug=True)
        result_dusts = await zadnegoale.async_get_dusts()
        result_alerts = await zadnegoale.async_get_alerts()

    await session.close()

    assert zadnegoale.region_name == "Karpaty"
    assert result_dusts.cladosporium.value == 5
    assert result_dusts.cladosporium.trend == "No change"
    assert result_dusts.cladosporium.level == "Very low"
    assert result_dusts.yew.value == 1
    assert result_dusts.yew.trend == "Increase"
    assert result_dusts.yew.level == "Lack"
    assert result_dusts.hazel.value == 5
    assert result_dusts.hazel.trend == "No change"
    assert result_dusts.hazel.level == "Very low"
    assert result_dusts.elm.value == 1
    assert result_dusts.elm.trend == "No change"
    assert result_dusts.elm.level == "Lack"
    assert result_dusts.willow.trend == "No change"
    assert result_dusts.willow.level == "Lack"
    assert result_alerts[0] == "Wysokie stężenie pyłku olszy, bardzo niskie leszczyny."


@pytest.mark.asyncio
async def test_invalid_region():
    """Test with invalid region."""
    session = aiohttp.ClientSession()

    try:
        ZadnegoAle(session, INVALID_REGION)
    except InvalidRegionError as error:
        assert str(error.status) == "'region' should be an integer from 1 to 9"

    await session.close()


@pytest.mark.asyncio
async def test_api_error():
    """Test API error."""
    session = aiohttp.ClientSession()

    with aioresponses() as session_mock, patch(
        "zadnegoale.date", today=Mock(return_value=TEST_DATE)
    ):
        session_mock.get(
            f"http://api.zadnegoale.pl/dusts/public/date/20210101/region/{VALID_REGION}",
            status=404,
        )
        zadnegoale = ZadnegoAle(session, VALID_REGION)
        try:
            await zadnegoale.async_get_dusts()
        except ApiError as error:
            assert str(error.status) == "Invalid response from Zadnego Ale API: 404"

    await session.close()


@pytest.mark.asyncio
async def test_invalid_data():
    """Test invalid data."""
    session = aiohttp.ClientSession()

    with aioresponses() as session_mock, patch(
        "zadnegoale.date", today=Mock(return_value=TEST_DATE)
    ):
        session_mock.get(
            f"http://api.zadnegoale.pl/dusts/public/date/20210101/region/{VALID_REGION}",
            payload="null",
        )
        zadnegoale = ZadnegoAle(session, VALID_REGION)
        try:
            await zadnegoale.async_get_dusts()
        except ApiError as error:
            assert str(error.status) == "Invalid response from Zadnego Ale API: null"

    await session.close()
