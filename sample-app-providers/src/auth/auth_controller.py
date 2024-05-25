from typing import Annotated

from nestipy.openapi.decorator import ApiTags, ApiOkResponse, ApiNotFoundResponse, ApiBody
from nestipy.common import Controller, Post
from nestipy.ioc import Inject, Body

from .auth_dto import LoginDto, RegisterDto
from .auth_service import AuthService


@Controller('auth')
@ApiTags('Auth')
@ApiOkResponse()
@ApiNotFoundResponse()
class AuthController:
    auth_service: Annotated[AuthService, Inject()]

    @ApiBody(RegisterDto)
    @Post('/register')
    async def register(self, data: Annotated[RegisterDto, Body()]) -> str:
        return await self.auth_service.register(data)

    @ApiBody(LoginDto)
    @Post('/login')
    async def login(self, data: Annotated[LoginDto, Body()]) -> str:
        return await self.auth_service.login(data)
