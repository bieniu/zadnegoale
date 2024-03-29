"""Example of usage."""
import asyncio
import logging

from aiohttp import ClientError, ClientSession

from zadnegoale import ApiError, InvalidRegionError, ZadnegoAle

REGION = 8

logging.basicConfig(level=logging.DEBUG)


async def main():
    """Main function."""
    async with ClientSession() as websession:
        try:
            zadnegoale = ZadnegoAle(websession, REGION, debug=False)
            dusts = await zadnegoale.async_get_dusts()
            alerts = await zadnegoale.async_get_alerts()

        except (ApiError, ClientError, InvalidRegionError) as error:
            print(f"Error: {error}")
        else:
            print(f"Region: {zadnegoale.region_name}")
            print(f"Dusts: {dusts}")
            print(f"Alerts: {alerts}")


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()
