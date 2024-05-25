from typing import Any, Annotated

from nestipy.websocket import IoAdapter, Gateway, SubscribeMessage, SuccessEvent
from nestipy.ioc import SocketServer, SocketClient, SocketData


@Gateway()
class AppGateway:
    server: Annotated[IoAdapter, SocketServer()]

    @SubscribeMessage('user')
    async def on_user(self, sid: Annotated[any, SocketClient()], data: Annotated[Any, SocketData()]):
        print(sid, data)
        await self.server.emit('user', data, sid)

    @SuccessEvent('message')
    @SubscribeMessage('message')
    async def on_message(self, sid: Annotated[any, SocketClient()], data: Annotated[Any, SocketData()]):
        print(sid, data)
        return "Hello from success event"
