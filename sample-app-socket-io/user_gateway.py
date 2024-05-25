from typing import Any, Annotated

from nestipy.websocket import IoAdapter, Gateway, SubscribeMessage
from nestipy.ioc import SocketServer, SocketClient, SocketData


@Gateway()
class UserGateway:
    server: Annotated[IoAdapter, SocketServer()]

    @SubscribeMessage('user')
    async def on_user(self, sid: Annotated[any, SocketClient()], data: Annotated[Any, SocketData()]):
        print(sid, data)
        await self.server.emit('user', data, sid)
