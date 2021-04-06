import asyncio
import logging

from aiohttp import ClientError, ClientSession

from zadnegoale import ApiError, InvalidRegionError, ZadnegoAle

REGION = 2

logging.basicConfig(level=logging.DEBUG)


async def main():
    async with ClientSession() as websession:
        try:
            zadnegoale = ZadnegoAle(websession, REGION)
            data = await zadnegoale.async_update(alerts=True)

        except (ApiError, ClientError, InvalidRegionError) as error:
            print(f"Error: {error}")
        else:
            print(f"Region: {zadnegoale.region_name}")
            print(f"Data: {data}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
