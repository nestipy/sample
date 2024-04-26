import os

from dotenv import dotenv_values
from nestipy.common import Injectable
from nestipy_ioc import Inject

from .builder import CONFIG2OPTION


@Injectable()
class Config2Service:
    options: Inject[CONFIG2OPTION]
    env: dict = []

    def __init__(self):
        env_directory = os.path.join(os.getcwd(), self.options.folder, '.env')
        self.env = dotenv_values(env_directory)

    def get(self, key: str):
        return self.env.get(key)
