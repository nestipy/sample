import uvicorn
from nestipy.openapi import DocumentBuilder, SwaggerModule

from app_module import AppModule
from app_middleware import AppMiddleware
from nestipy.core import NestipyFactory

app = NestipyFactory.create(AppModule)

document = DocumentBuilder().set_title('API Providers') \
    .set_description('The API description').set_version('1.0').add_bearer_auth().add_basic_auth().build()
SwaggerModule.setup('api', app, document)

app.use(AppMiddleware)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
