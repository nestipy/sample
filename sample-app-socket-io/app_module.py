from nestipy.common import Module

from app_controller import AppController
from app_gateway import AppGateway
from app_service import AppService


@Module(
    controllers=[
        AppController
    ],
    providers=[
        AppService,
        AppGateway
    ]
)
class AppModule:
    ...
