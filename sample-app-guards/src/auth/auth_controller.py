from nestipy.openapi.decorator import ApiBody, ApiCreatedResponse
from nestipy.common import Controller, Post
from nestipy_ioc import Inject, Body

from .auth_dto import LoginDto, RegisterDto
from .auth_service import AuthService


@ApiCreatedResponse()
@Controller('auth')
class AuthController:
    auth_service: Inject[AuthService]

    @ApiBody(LoginDto)
    @Post('/login')
    async def login(self, data: Body[LoginDto]) -> str:
        return await self.auth_service.login(data)

    @ApiBody(RegisterDto)
    @Post('/register')
    async def register(self, data: Body[RegisterDto]) -> str:
        return await self.auth_service.register(data)
