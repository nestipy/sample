from nestipy_decorator import Module

from .builder import ConfigurableModuleClass, JwtOption
from .jwt_service import JwtService


@Module(
    providers=[
        JwtService
    ],
    exports=[
        JwtService
    ]
)
class JwtModule(ConfigurableModuleClass):
    ...


__all__ = [
    "JwtModule",
    "JwtOption",
    "JwtService"
]
