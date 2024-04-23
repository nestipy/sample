from nestipy.common import UseGuards, Request
from nestipy.openapi.decorator import ApiCreatedResponse, ApiOkResponse, ApiBearerAuth, ApiBody
from nestipy_decorator import Controller, Get, Post, Put, Delete
from nestipy_ioc import Inject, Body, Params, Req

from .user_dto import CreateUserDto, UpdateUserDto
from .user_service import UserService
from ..guards import AuthGuard


@ApiBearerAuth()
@ApiOkResponse()
@ApiCreatedResponse()
@UseGuards(AuthGuard)
@Controller('users')
class UserController:
    user_service: Inject[UserService]

    @Get()
    async def list(self, req: Req[Request]) -> str:
        print(req.user)
        return await self.user_service.list()

    @ApiBody(CreateUserDto)
    @Post()
    async def create(self, data: Body[CreateUserDto]) -> str:
        return await self.user_service.create(data)

    @ApiBody(UpdateUserDto)
    @Put('/{user_id}')
    async def update(self, user_id: Params[int], data: Body[UpdateUserDto]) -> str:
        return await self.user_service.update(user_id, data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Params[int]) -> None:
        return await self.user_service.delete(user_id)
