from nestipy.common import Controller, Post
from nestipy.openapi.decorator import ApiTags, ApiOkResponse, ApiNotFoundResponse, ApiBody
from nestipy.types_ import Inject, Body

from .auth_dto import LoginDto, RegisterDto
from .auth_service import AuthService


@Controller('auth')
@ApiTags('Auth')
@ApiOkResponse()
@ApiNotFoundResponse()
class AuthController:
    auth_service: Inject[AuthService]

    @ApiBody(RegisterDto)
    @Post('/register')
    async def register(self, data: Body[RegisterDto]) -> str:
        return await self.auth_service.register(data)

    @ApiBody(LoginDto)
    @Post('/login')
    async def login(self, data: Body[LoginDto]) -> str:
        return await self.auth_service.login(data)
