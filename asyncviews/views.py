import asyncio
from time import sleep
import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as Client:
        r = await Client.get('https://httpbin.org')
        print(r)


def http_call_sync():
    for num in range(1, 11):
        sleep(1)
        print(num)
    r = httpx.get('https://httpbin.org')
    print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    await loop.create_task(http_call_async())
    return HttpResponse('Exercício Modulo 11')


def sync_view(request):
    http_call_sync()
    return HttpResponse('Blocking HTTP request')
