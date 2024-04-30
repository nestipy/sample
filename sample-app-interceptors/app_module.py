from nestipy.common import Module
from nestipy.core import AppKey
from nestipy.ioc import ModuleProviderDict

from app_controller import AppController
from app_service import AppService
from interceptor.test import TestInterceptor


@Module(
    controllers=[AppController],
    providers=[
        ModuleProviderDict(token=AppKey.APP_INTERCEPTOR, use_class=TestInterceptor),
        AppService
    ]
)
class AppModule:
    ...
