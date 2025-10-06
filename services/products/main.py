import asyncpg
import functools
from aiohttp import web

from utils.db import DB_KEY, create_database_pool, destroy_database_pool

routes = web.RouteTableDef()


@routes.get("/products")
async def products(request: web.Request) -> web.Response:
    db: asyncpg.Connection = request.app[DB_KEY]
    product_query = "SELECT product_id, product_name FROM product"
    result = await db.fetch(product_query)
    return web.json_response(dict(record) for record in result)


app = web.Application()
app.on_startup.append(
    functools.partial(  # type: ignore[reportArgumentType]
        create_database_pool,
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="password",
        database="favorites",
    )
)
app.on_cleanup.append(destroy_database_pool)
app.add_routes(routes)
web.run_app(app, port=8000)
