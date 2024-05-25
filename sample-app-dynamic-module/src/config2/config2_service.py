import os
from typing import Annotated

from dotenv import dotenv_values
from nestipy.common import Injectable
from nestipy.ioc import Inject

from .builder import CONFIG2OPTION, Config2Option


@Injectable()
class Config2Service:
    options: Annotated[Config2Option, Inject(CONFIG2OPTION)]
    env: dict = []

    def __init__(self):
        env_directory = os.path.join(os.getcwd(), self.options.folder, '.env')
        self.env = dotenv_values(env_directory)

    def get(self, key: str):
        return self.env.get(key)
