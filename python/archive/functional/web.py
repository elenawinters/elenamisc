"""
    This HTTPX wrapper was written by Elena Winters, 2018-2025

"""

import httpx

httpxcept = (httpx._exceptions.WriteError,
             httpx._exceptions.ConnectTimeout,
             httpx._exceptions.ReadTimeout,
             httpx._exceptions.ConnectError,
             ConnectionResetError,
             Exception)


class Client:
    def __init__(self, url, **kwargs):
        self.limit = int(kwargs.get('limit', 3))
        self.url = url

    def process(self, exc):
        print(exc)

    def post(self, **kwargs):
        for x in range(1, self.limit + 1):
            try:
                with httpx.Client() as client:
                    client.post(url=self.url, **kwargs)
                return

            except httpxcept as exc:
                self.process(exc)

    def get(self, **kwargs):
        for x in range(1, self.limit + 1):
            try:
                with httpx.Client() as client:
                    r = client.get(url=self.url, **kwargs)
                return r

            except httpxcept as exc:
                self.process(exc)

        return None

    async def async_post(self, **kwargs):
        for x in range(1, self.limit + 1):
            try:
                async with httpx.AsyncClient() as client:
                    await client.post(url=self.url, **kwargs)
                return

            except httpxcept as exc:
                self.process(exc)

    async def async_get(self, **kwargs):
        for x in range(1, self.limit + 1):
            try:
                async with httpx.AsyncClient() as client:
                    r = await client.get(url=self.url, **kwargs)
                return r

            except httpxcept as exc:
                self.process(exc)

        return None


Request = Client