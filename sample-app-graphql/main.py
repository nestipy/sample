import uvicorn

from app_module import AppModule
from nestipy.core import NestipyFactory

app = NestipyFactory.create(AppModule)
app.enable_cors()

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
