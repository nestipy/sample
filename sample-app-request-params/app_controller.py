from dataclasses import dataclass

from nestipy.openapi.decorator import ApiTags, ApiOkResponse, ApiNotFoundResponse
from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy_ioc import Inject, Body, Params

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
    service: Inject[AppService]

    @Get()
    async def get(self) -> str:
        return await self.service.get()

    @Post()
    async def post(self, data: Body[CreateTest]) -> str:
        return await self.service.post(data=data)

    @Put('/{user_id}')
    async def put(self, user_id: Params[int], data: Body[UpdateTest]) -> str:
        return await self.service.put(id_=user_id, data=data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Params[int]) -> None:
        await self.service.delete(id_=user_id)
