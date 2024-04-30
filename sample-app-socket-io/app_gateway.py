from typing import Any

from nestipy.websocket import IoAdapter, Gateway, SubscribeMessage, SuccessEvent
from nestipy.ioc import SocketServer, SocketClient, SocketData


@Gateway()
class AppGateway:
    server: SocketServer[IoAdapter]

    @SubscribeMessage('user')
    async def on_user(self, sid: SocketClient[str], data: SocketData[Any]):
        print(sid, data)
        await self.server.emit('user', data, sid)

    @SuccessEvent('message')
    @SubscribeMessage('message')
    async def on_message(self, sid: SocketClient[str], data: SocketData[Any]):
        print(sid, data)
        return "Hello from success event"
