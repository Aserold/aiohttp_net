from aiohttp import web


app = web.Application()


async def hello_world(request):
    return web.json_response({'message': 'Hello World!'})


app.add_routes(
    [
        web.get('/hello/world', hello_world),
        web.post('/hello/world', hello_world)
        ]
    )

web.run_app(app)