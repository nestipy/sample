from nestipy.openapi.decorator import ApiTags, ApiOkResponse, ApiNotFoundResponse, ApiBody
from nestipy_decorator import Controller, Get, Post, Put, Delete
from nestipy_ioc import Inject, Body, Params

from app_service import AppService


@Controller()
@ApiTags('App')
@ApiOkResponse()
@ApiNotFoundResponse()
class AppController:
    service: Inject[AppService]

    @Get()
    async def get(self) -> str:
        return await self.service.get()

    @ApiBody()
    @Post()
    async def post(self, data: Body[dict]) -> str:
        return await self.service.post(data=data)

    @ApiBody()
    @Put('/{user_id}')
    async def put(self, user_id: Params[int], data: Body[dict]) -> str:
        return await self.service.put(id_=user_id, data=data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Params[int]) -> None:
        await self.service.delete(id_=user_id)
