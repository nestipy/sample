from typing import Annotated

from nestipy.common import Injectable
from nestipy.ioc import Inject

from .user_dto import CreateUserDto, UpdateUserDto
from ..config.config_service import ConfigService
from ..config2.config2_service import Config2Service


@Injectable()
class UserService:
    config: Annotated[ConfigService, Inject()]
    config2: Annotated[Config2Service, Inject()]

    async def list(self):
        return "test"

    async def create(self, data: CreateUserDto):
        return "test"

    async def update(self, id: int, data: UpdateUserDto):
        return "test"

    async def delete(self, id: int):
        return "test"
