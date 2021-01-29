import json

from aiohttp import web


async def index(request: web.Request):
    raw_data = json.dumps({'status': 200})
    headers = {'Content-Type': 'application/json'}
    return web.Response(body=raw_data, headers=headers)
