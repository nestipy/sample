from dataclasses import dataclass, field
from datetime import datetime
from typing import Union

from nestipy_dynamic_module import ConfigurableModuleBuilder


@dataclass
class JwtOption:
    secret: str
    exp: Union[datetime, int,]
    algorithms: list[str] = field(default_factory=lambda: ['HS256'])


ConfigurableModuleClass, JWT_OPTION_TOKEN = ConfigurableModuleBuilder[JwtOption]().set_method('for_root').build()
