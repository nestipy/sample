from typing import Annotated

from nestipy.common import HttpException, HttpStatusMessages, HttpStatus
from nestipy.common import Injectable
from nestipy.ioc import Inject

from .auth_dto import LoginDto, RegisterDto
from ..jwt.jwt_module import JwtService
from ..user.user_service import UserService


@Injectable()
class AuthService:
    user_service: Annotated[UserService, Inject()]
    jwt_service: Annotated[JwtService, Inject()]

    async def login(self, data: LoginDto):
        user = await self.user_service.find_by_email(data.email)
        if user is not None:
            return await self.jwt_service.sign(user)
        else:
            raise HttpException(HttpStatus.UNAUTHORIZED, HttpStatusMessages.UNAUTHORIZED)

    async def register(self, data: RegisterDto):
        return await self.user_service.create(data)
