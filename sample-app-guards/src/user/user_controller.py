from typing import Annotated

from nestipy.common import UseGuards, Request
from nestipy.openapi.decorator import ApiCreatedResponse, ApiOkResponse, ApiBearerAuth, ApiBody
from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.ioc import Inject, Body, Param, Req

from .user_dto import CreateUserDto, UpdateUserDto
from .user_service import UserService
from ..guards import AuthGuard


@ApiBearerAuth()
@ApiOkResponse()
@ApiCreatedResponse()
@UseGuards(AuthGuard)
@Controller('users')
class UserController:
    user_service: Annotated[UserService, Inject()]

    @Get()
    async def list(self, req: Annotated[Request, Req()]) -> str:
        print(req.user)
        return await self.user_service.list()

    @ApiBody(CreateUserDto)
    @Post()
    async def create(self, data: Annotated[CreateUserDto, Body()]) -> str:
        return await self.user_service.create(data)

    @ApiBody(UpdateUserDto)
    @Put('/{user_id}')
    async def update(self, user_id: Annotated[int, Param('user_id')], data: Annotated[UpdateUserDto, Body()]) -> str:
        return await self.user_service.update(user_id, data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Annotated[int, Param()]) -> None:
        return await self.user_service.delete(user_id)
