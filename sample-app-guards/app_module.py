from datetime import timezone, datetime, timedelta

from nestipy_decorator import Module

from app_controller import AppController
from app_service import AppService
from src.auth.auth_module import AuthModule
from src.jwt.jwt_module import JwtModule, JwtOption
from src.user.user_module import UserModule


@Module(

    imports=[
        JwtModule.for_root(JwtOption(
            secret='test_secret',
            exp=datetime.now(tz=timezone.utc) + timedelta(hours=24),
        )),
        AuthModule,
        UserModule,
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
