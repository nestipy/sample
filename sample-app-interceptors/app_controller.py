from nestipy.common import Controller, Get, Post, Put, Delete, UseInterceptors
from nestipy.ioc import Inject, Body, Params

from app_service import AppService
from interceptor.test import TestInterceptor

@UseInterceptors(TestInterceptor)
@Controller()
class AppController:
    service: Inject[AppService]

    @UseInterceptors(TestInterceptor)
    @Get()
    async def get(self) -> str:
        return await self.service.get()

    @Post()
    async def post(self, data: Body[dict]) -> str:
        return await self.service.post(data=data)

    @Put('/{app_id}')
    async def put(self, app_id: Params[int], data: Body[dict]) -> str:
        return await self.service.put(id_=app_id, data=data)

    @Delete('/{app_id}')
    async def delete(self, app_id: Params[int]) -> None:
        await self.service.delete(id_=app_id)
