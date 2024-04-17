import uvicorn
from nestipy.core.nestipy_factory import NestipyFactory
from nestipy.core.platform import NestipyBlackSheepApplication

from app_module import AppModule

app = NestipyFactory[NestipyBlackSheepApplication].create(AppModule)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
