from nestipy_decorator import Module

from .user_controller import UserController
from .user_service import UserService


@Module(
    providers=[UserService],
    controllers=[UserController],
    exports=[UserService]
)
class UserModule:
    ...
