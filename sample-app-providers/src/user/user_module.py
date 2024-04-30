from nestipy.common import Module
from nestipy.ioc import ModuleProviderDict

from .user_controller import UserController
from .user_service import UserService


@Module(
    providers=[
        UserService,
        ModuleProviderDict(
            token='TEST',
            value='Test value'
        )
    ],
    controllers=[UserController],
    exports=[
        UserService,
        'TEST'
    ]
)
class UserModule:
    ...
