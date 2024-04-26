from nestipy.common import Module

from .builder import ConfigurableModuleClass
from .config2_service import Config2Service


@Module(
    providers=[
        Config2Service
    ],
    exports=[
        Config2Service
    ],
    is_global=True
)
class Config2Module(ConfigurableModuleClass):
    ...
