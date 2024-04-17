from nestipy.common import Injectable
from nestipy.types_ import Inject

from ..user.user_service import UserService
from  ..user.user_dto import CreateUserDto
from .auth_dto import LoginDto, RegisterDto


@Injectable()
class AuthService:
    user_service: Inject[UserService]

    async def login(self, data: LoginDto):
        await self.user_service.get(data.password)
        return data

    async def register(self, data: RegisterDto):
        await self.user_service.create(data)
        return data
