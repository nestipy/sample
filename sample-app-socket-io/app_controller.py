from nestipy.common import Controller, Get, Post, Put, Delete, Render
from nestipy_ioc import Inject, Body, Params

from app_service import AppService


@Controller()
class AppController:
    service: Inject[AppService]

    @Render('index.html')
    @Get()
    async def get(self) -> dict:
        return {
            'title': "Nestipy socketio"
        }

    @Post()
    async def post(self, data: Body[dict]) -> str:
        return await self.service.post(data=data)

    @Put('/{app_id}')
    async def put(self, app_id: Params[int], data: Body[dict]) -> str:
        return await self.service.put(id_=app_id, data=data)

    @Delete('/{app_id}')
    async def delete(self, app_id: Params[int]) -> None:
        await self.service.delete(id_=app_id)