from bot.misc import executor
from server.routes import setup_routes


def init_app(app):
    setup_routes(app)
    return app
