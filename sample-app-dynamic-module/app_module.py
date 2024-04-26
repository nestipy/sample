from nestipy.common import Module

from app_controller import AppController
from app_service import AppService
from src.config.config_module import ConfigModule, ConfigOption
from src.config2.builder import Config2Option
from src.config2.config2_module import Config2Module
from src.user.user_module import UserModule


async def config2module_factory():
    return Config2Option(folder='./')


@Module(
    imports=[
        ConfigModule.register(ConfigOption(folder='./')),
        Config2Module.register_async(
            factory=config2module_factory
        ),
        UserModule,
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
