from typing import Annotated

from nestipy.common import Injectable
from nestipy.ioc import Inject

from src.config.config_service import ConfigService
from src.config2.config2_service import Config2Service


@Injectable()
class AppService:
    config: Annotated[ConfigService, Inject()]
    config2: Annotated[Config2Service, Inject()]

    @classmethod
    async def get(cls):
        return "test"

    @classmethod
    async def post(cls, data: dict):
        return "test"

    @classmethod
    async def put(cls, id_: int, data: dict):
        return "test"

    @classmethod
    async def delete(cls, id_: int):
        return "test"
