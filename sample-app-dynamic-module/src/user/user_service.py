from nestipy.common import Injectable
from nestipy_ioc import Inject

from .user_dto import CreateUserDto, UpdateUserDto
from ..config.config_service import ConfigService
from ..config2.config2_service import Config2Service


@Injectable()
class UserService:
    config: Inject[ConfigService]
    config2: Inject[Config2Service]

    async def list(self):
        return "test"

    async def create(self, data: CreateUserDto):
        return "test"

    async def update(self, id: int, data: UpdateUserDto):
        return "test"

    async def delete(self, id: int):
        return "test"
