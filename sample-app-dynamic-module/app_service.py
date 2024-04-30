from nestipy.common import Injectable
from nestipy.ioc import Inject

from src.config.config_service import ConfigService
from src.config2.config2_service import Config2Service


@Injectable()
class AppService:
    config: Inject[ConfigService]
    config2: Inject[Config2Service]

    @classmethod
    async def get(cls):
        return "test"

    @classmethod
    async def post(cls, data: str):
        return "test"

    @classmethod
    async def put(cls, id_: int, data: str):
        return "test"

    @classmethod
    async def delete(cls, id_: int):
        return "test"
