import uvicorn
from nestipy.core import NestipyFactory

from app_module import AppModule
from interceptor.test import TestInterceptor

app = NestipyFactory.create(AppModule)

app.use_global_interceptors(TestInterceptor)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
