from typing import Annotated

from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.common import UseFilters, HttpException, HttpStatus, HttpStatusMessages
from nestipy.ioc import Inject, Body, Param

from app_service import AppService
from exception.badrequest_filter import BadRequestExceptionFilter, BadRequestException


@UseFilters(BadRequestExceptionFilter)
@Controller()
class AppController:
    service: Annotated[AppService, Inject()]

    @Get()
    async def get(self) -> str:
        raise BadRequestException()
        # return await self.service.get()

    @Get('/other')
    async def get2(self) -> str:
        raise HttpException(HttpStatus.BAD_REQUEST, HttpStatusMessages.BAD_REQUEST)

    @Post()
    async def post(self, data: Annotated[dict, Body()]) -> str:
        return await self.service.post(data=data)

    @Put('/{app_id}')
    async def put(self, app_id: Annotated[int, Param()], data: Annotated[dict, Body()]) -> str:
        return await self.service.put(id_=app_id, data=data)

    @Delete('/{app_id}')
    async def delete(self, app_id: Annotated[int, Param()]) -> None:
        await self.service.delete(id_=app_id)
