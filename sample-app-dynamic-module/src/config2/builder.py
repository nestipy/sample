from dataclasses import dataclass

from nestipy.dynamic_module import ConfigurableModuleBuilder


@dataclass
class Config2Option:
    folder: str


ConfigurableModuleClass, CONFIG2OPTION = ConfigurableModuleBuilder[Config2Option]().build()
