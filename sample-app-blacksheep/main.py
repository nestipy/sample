import uvicorn
from nestipy.core import NestipyBlackSheepApplication
from nestipy.core import NestipyFactory

from app_module import AppModule

app = NestipyFactory[NestipyBlackSheepApplication].create(AppModule)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
