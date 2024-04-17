from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.openapi.decorator import ApiTags, ApiNotFoundResponse, ApiOkResponse, ApiBearerAuth, ApiBody
from nestipy.types_ import Inject, Body, Params

from .user_dto import CreateUserDto, UpdateUserDto
from .user_service import UserService


@Controller('users')
@ApiTags('User')
@ApiOkResponse()
@ApiNotFoundResponse()
@ApiBearerAuth()
class UserController:
    user_service: Inject[UserService]

    @Get()
    async def list(self) -> str:
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