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
    with open("tests/data/dusts.json") as file:
        dusts = json.load(file)
    with open("tests/data/alerts.json") as file:
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

        zadnegoale = ZadnegoAle(session, VALID_REGION)
        result = await zadnegoale.async_update(alerts=True)

    await session.close()

    assert zadnegoale.region_name == "Karpaty"
    assert len(result.sensors) == 8
    assert result.sensors.cladosporium["value"] == 5
    assert result.sensors.cladosporium["trend"] == "bez zmian"
    assert result.sensors.cladosporium["level"] == "bardzo niskie"
    assert result.sensors.cis["value"] == 1
    assert result.sensors.cis["trend"] == "wzrost"
    assert result.sensors.cis["level"] == "brak"
    assert result.sensors.leszczyna["value"] == 5
    assert result.sensors.leszczyna["trend"] == "bez zmian"
    assert result.sensors.leszczyna["level"] == "bardzo niskie"
    assert result.sensors.wiąz["value"] == 1
    assert result.sensors.wiąz["trend"] == "bez zmian"
    assert result.sensors.wiąz["level"] == "brak"
    assert result.sensors.wierzba["value"] == 1
    assert result.sensors.wierzba["trend"] == "bez zmian"
    assert result.sensors.wierzba["level"] == "brak"
    assert (
        result.alerts["value"]
        == "Wysokie stężenie pyłku olszy, bardzo niskie leszczyny."
    )
    try:
        result.sensors.unknown
    except AttributeError as error:
        assert str(error) == "No such attribute: unknown"


@pytest.mark.asyncio
async def test_dusts():
    """Test with valid dusts data."""
    with open("tests/data/dusts.json") as file:
        dusts = json.load(file)

    session = aiohttp.ClientSession()

    with aioresponses() as session_mock, patch(
        "zadnegoale.date", today=Mock(return_value=TEST_DATE)
    ):
        session_mock.get(
            f"http://api.zadnegoale.pl/dusts/public/date/20210101/region/{VALID_REGION}",
            payload=dusts,
        )

        zadnegoale = ZadnegoAle(session, VALID_REGION)
        result = await zadnegoale.async_update()

    await session.close()

    assert zadnegoale.region_name == "Karpaty"
    assert len(result.sensors) == 8
    assert result.sensors.cladosporium["value"] == 5
    assert result.sensors.cladosporium["trend"] == "bez zmian"
    assert result.sensors.cladosporium["level"] == "bardzo niskie"
    assert result.sensors.cis["value"] == 1
    assert result.sensors.cis["trend"] == "wzrost"
    assert result.sensors.cis["level"] == "brak"
    assert result.sensors.leszczyna["value"] == 5
    assert result.sensors.leszczyna["trend"] == "bez zmian"
    assert result.sensors.leszczyna["level"] == "bardzo niskie"
    assert result.sensors.wiąz["value"] == 1
    assert result.sensors.wiąz["trend"] == "bez zmian"
    assert result.sensors.wiąz["level"] == "brak"
    assert result.sensors.wierzba["value"] == 1
    assert result.sensors.wierzba["trend"] == "bez zmian"
    assert result.sensors.wierzba["level"] == "brak"


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
            await zadnegoale.async_update()
        except ApiError as error:
            assert str(error.status) == "Invalid response from Zadnego Ale API: 404"

    await session.close()
