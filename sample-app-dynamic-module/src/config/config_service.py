import os.path
from dataclasses import dataclass

from dotenv import dotenv_values
from nestipy.common import Injectable
from nestipy_ioc import Inject


@dataclass
class ConfigOption:
    folder: str


@Injectable()
class ConfigService:
    options: Inject['CONFIG_OPTION']
    env: dict = []

    def __init__(self):
        env_directory = os.path.join(os.getcwd(), self.options.folder, '.env')
        self.env = dotenv_values(env_directory)

    def get(self, key: str):
        return self.env.get(key)
