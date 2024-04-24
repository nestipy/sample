import uvicorn
from nestipy.openapi import DocumentBuilder, SwaggerModule

from app_module import AppModule
from nestipy.core import NestipyFactory

app = NestipyFactory.create(AppModule)

document = DocumentBuilder().set_title('Example API') \
    .set_description('The API description').set_version('1.0').add_bearer_auth().add_basic_auth().build()
SwaggerModule.setup('api', app, document)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
