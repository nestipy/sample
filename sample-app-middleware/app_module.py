from nestipy_decorator import Module

from app_controller import AppController
from app_service import AppService
from src.user.user_module import UserModule


@Module(
    imports=[
        UserModule
    ],
    controllers=[AppController],
    providers=[
        AppService
    ]
)
class AppModule:
    ...
