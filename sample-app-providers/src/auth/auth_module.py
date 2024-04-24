from nestipy.common import Module

from .auth_controller import AuthController
from .auth_service import AuthService
from ..user.user_module import UserModule


@Module(
    providers=[AuthService],
    controllers=[AuthController],
    imports=[UserModule]
)
class AuthModule:
    ...
