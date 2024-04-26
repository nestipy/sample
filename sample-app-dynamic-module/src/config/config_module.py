from nestipy.common import Module, ModuleProviderDict
from nestipy_dynamic_module import DynamicModule

from .config_service import ConfigService, ConfigOption


@Module()
class ConfigModule:

    @classmethod
    def register(cls, options: ConfigOption) -> DynamicModule:
        return DynamicModule(
            module=cls,
            providers=[
                ModuleProviderDict(
                    token='CONFIG_OPTION',
                    value=options
                ),
                ConfigService
            ],
            controllers=[],
            imports=[],
            is_global=False,
            exports=[
                ConfigService
            ]
        )
