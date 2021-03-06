import functools
import traceback
import httpx


httpxcept = (httpx._exceptions.WriteError,
             httpx._exceptions.ConnectTimeout,
             httpx._exceptions.ReadTimeout,
             httpx._exceptions.ConnectError,
             ConnectionResetError,
             Exception)


def retry(method):  # this implements the retry functionality in a better way
    @functools.wraps(method)
    def _retry(self, *args, **kwargs):
        for _ in range(1, self.limit + 1):
            try:
                return method(self, *args, **kwargs)
            except httpxcept as exc:
                self.process(exc)
        return self
    return _retry


class Client:
    def __init__(self, url, **kwargs):
        self.limit = int(kwargs.get('limit', 3))
        self.url = url

    def json(self):  # returns None if it fails to return anything in the retry
        return None  # this prevents a potentially fatal error from occuring

    def process(self, exc):
        traceback.print_exc()

    @retry
    def post(self, **kwargs):
        with httpx.Client() as client:
            client.post(url=self.url, **kwargs)
        return

    @retry
    def get(self, **kwargs):
        with httpx.Client() as client:
            r = client.get(url=self.url, **kwargs)
        return r

    @retry
    async def async_post(self, **kwargs):
        async with httpx.AsyncClient() as client:
            await client.post(url=self.url, **kwargs)
        return

    @retry
    async def async_get(self, **kwargs):
        async with httpx.AsyncClient() as client:
            r = await client.get(url=self.url, **kwargs)
        return r


# class API(Client):
#     def __init__(self, loc='', **kwargs):
#         pre = f"http://{json.orm['api']['host']}:{json.orm['api']['port']}/{loc}"
#         super().__init__(pre, **kwargs)


# api = API


Request = Client
