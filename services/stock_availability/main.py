import asyncio
import random
from aiohttp import web


routes = web.RouteTableDef()


@routes.get("/products/{id}/inventory")
async def get_inventory(request: web.Request) -> web.Response:
    delay: int = random.randint(0, 5)
    await asyncio.sleep(delay)
    inventory: int = random.randint(0, 100)
    return web.json_response({"inventory": inventory})


if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=8001)
