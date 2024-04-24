from nestipy.openapi.decorator import ApiTags, ApiOkResponse, ApiNotFoundResponse, ApiBody
from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy_ioc import Inject, Body, Params

from .user_dto import CreateUserDto, UpdateUserDto
from .user_service import UserService


@ApiTags('User')
@ApiOkResponse()
@ApiNotFoundResponse()
@Controller('users')
class UserController:
    user_service: Inject[UserService]

    @Get()
    async def list(self) -> str:
        return await self.user_service.list()

    @ApiBody(CreateUserDto, consumer='multipart/form-data')
    @Post()
    async def create(self, data: Body[CreateUserDto]) -> str:
        return await self.user_service.create(data)

    @ApiBody(CreateUserDto, consumer='multipart/form-data')
    @Put('/{user_id}')
    async def update(self, user_id: Params[int], data: Body[UpdateUserDto]) -> str:
        return await self.user_service.update(user_id, data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Params[int]) -> None:
        return await self.user_service.delete(user_id)
