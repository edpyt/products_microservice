from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/user/{id}/favorites")
async def favorites(request: web.Request) -> web.Response:
    try:
        str_id = request.match_info["id"]
        db = request.app[DB_KEY]
        return web.json_response([])
    except ValueError:
        raise web.HTTPBadRequest()
