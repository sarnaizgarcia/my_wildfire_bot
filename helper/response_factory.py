from flask import Response


def response_factory(response):
    web_response = Response(
        response.get('message'),
        status=response.get('status')
    )

    web_response.headers['Content-Type'] = 'application/json'
    web_response.headers['Access-Control-Allow-Origin'] = '*'

    return web_response
