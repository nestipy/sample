import os

import socketio
import uvicorn
from nestipy.core import NestipyFactory, NestipyBlackSheepApplication
from nestipy.websocket import SocketIoAdapter

from app_module import AppModule

app = NestipyFactory[NestipyBlackSheepApplication].create(AppModule)
sio = socketio.AsyncServer(async_mode='asgi')
app.use_io_adapter(SocketIoAdapter(sio))

# serve static file
app.use_static_assets(os.path.join(os.path.dirname(__file__), 'public'))

# Template rendering
app.set_base_view_dir(os.path.join(os.path.dirname(__file__), 'views'))
app.set_view_engine('minijinja')

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
