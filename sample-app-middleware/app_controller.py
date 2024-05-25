from typing import Annotated

from nestipy.openapi.decorator import ApiTags, ApiOkResponse, ApiNotFoundResponse
from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.ioc import Inject, Body, Param

from app_service import AppService


@ApiTags('App')
@ApiOkResponse()
@ApiNotFoundResponse()
@Controller()
class AppController:
    service: Annotated[AppService, Inject()]

    @Get()
    async def get(self) -> str:
        return await self.service.get()

    @Post()
    async def post(self, data: Annotated[dict, Body()]) -> str:
        return await self.service.post(data=data)

    @Put('/{user_id}')
    async def put(self, user_id: Annotated[int, Param('user_id')], data: Annotated[dict, Body()]) -> str:
        return await self.service.put(id_=user_id, data=data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Annotated[int, Param('user_id')]) -> None:
        await self.service.delete(id_=user_id)
