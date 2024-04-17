from nestipy.common import Module

from .user_service import UserService
from .user_controller import UserController


@Module(
    providers=[UserService],
    controllers=[UserController],
    exports=[UserService]
)
class UserModule:
    ...
