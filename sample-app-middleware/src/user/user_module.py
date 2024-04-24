from nestipy.common import Module
from nestipy.core import MiddlewareConsumer
from nestipy_dynamic_module import NestipyModule

from .user_controller import UserController
from .user_middleware import UserMiddleware, user_middleware
from .user_service import UserService


@Module(
    providers=[UserService],
    controllers=[UserController]
)
class UserModule(NestipyModule):
    def configure(self, consumer: MiddlewareConsumer):
        consumer.apply(UserMiddleware, user_middleware).for_route(UserController, method=['POST']).excludes()
