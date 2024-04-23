from nestipy_decorator import Module

from .auth_controller import AuthController
from .auth_service import AuthService
from ..jwt.jwt_module import JwtModule
from ..user.user_module import UserModule


@Module(
    imports=[
        JwtModule,
        UserModule
    ],
    providers=[AuthService],
    controllers=[AuthController]
)
class AuthModule:
    ...
