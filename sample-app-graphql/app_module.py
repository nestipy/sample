from nestipy.common import Module, ModuleProviderDict
from nestipy.graphql import GraphqlModule, GraphqlOption

from app_controller import AppController
from app_service import AppService
from src.pubsub import PubSub
from src.user.user_module import UserModule


@Module(
    imports=[
        GraphqlModule.for_root(
            GraphqlOption(
                url='/graphql', ide='default'
            )
        ),
        UserModule
    ],
    controllers=[AppController],
    providers=[
        ModuleProviderDict(
            token=PubSub,
            value=PubSub()
        ),
        AppService
    ]
)
class AppModule:
    ...
