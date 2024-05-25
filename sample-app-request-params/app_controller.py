from dataclasses import dataclass
from typing import Annotated

from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.ioc import Inject, Body, Param
from nestipy.openapi.decorator import ApiTags, ApiOkResponse, ApiNotFoundResponse, ApiBody

from app_service import AppService


@dataclass
class CreateTest:
    name: str


@dataclass
class UpdateTest:
    name: str


@Controller()
@ApiTags('App')
@ApiOkResponse()
@ApiNotFoundResponse()
class AppController:
    service: Annotated[AppService, Inject()]

    @Get()
    async def get(self) -> str:
        return await self.service.get()

    @ApiBody(CreateTest)
    @Post()
    async def post(self, data: Annotated[CreateTest, Body()]) -> str:
        return await self.service.post(data=data)

    @ApiBody(CreateTest)
    @Put('/{user_id}')
    async def put(self, user_id: Annotated[int, Param('user_id')], data: Annotated[UpdateTest, Body()]) -> str:
        return await self.service.put(id_=user_id, data=data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Annotated[int, Param('user_id')]) -> None:
        await self.service.delete(id_=user_id)
