[![GitHub Release][releases-shield]][releases]
[![PyPI][pypi-releases-shield]][pypi-releases]
[![PyPI - Downloads][pypi-downloads]][pypi-statistics]
[![Buy me a coffee][buy-me-a-coffee-shield]][buy-me-a-coffee]
[![PayPal_Me][paypal-me-shield]][paypal-me]

# zadnegoale
Python wrapper for getting allergen concentration data from [Żadnego Ale](http://zadnegoale.pl)


## How to use package

```python
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

```
[releases]: https://github.com/bieniu/zadnegoale/releases
[releases-shield]: https://img.shields.io/github/release/bieniu/zadnegoale.svg?style=popout
[pypi-releases]: https://pypi.org/project/zadnegoale/
[pypi-statistics]: https://pepy.tech/project/zadnegoale
[pypi-releases-shield]: https://img.shields.io/pypi/v/zadnegoale
[pypi-downloads]: https://pepy.tech/badge/zadnegoale/month
[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/QnLdxeaqO
[paypal-me-shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal-me]: https://www.paypal.me/bieniu79
