from nestipy.common import Module

from .user_controller import UserController
from .user_service import UserService
from ..config.config_module import ConfigModule


@Module(
    imports=[ConfigModule],
    providers=[UserService],
    controllers=[UserController]
)
class UserModule:
    ...
