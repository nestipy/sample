from nestipy_decorator import Module

from app_controller import AppController
from app_service import AppService
from src.auth.auth_module import AuthModule
from src.user.user_module import UserModule


@Module(

    imports=[
        UserModule,
        AuthModule
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
