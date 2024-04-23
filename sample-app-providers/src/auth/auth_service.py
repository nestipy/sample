from nestipy_decorator import Injectable
from nestipy_ioc import Inject

from .auth_dto import LoginDto, RegisterDto
from ..user.user_service import UserService


@Injectable()
class AuthService:
    user_service: Inject[UserService]
    test: Inject["TEST"]

    async def login(self, data: LoginDto):
        await self.user_service.get(data.password)
        print(self.test)
        return data

    async def register(self, data: RegisterDto):
        await self.user_service.create(data)
        return data
