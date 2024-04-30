from nestipy.common import Injectable
from nestipy.common import NestipyMiddleware
from nestipy.common import Request, Response
from nestipy.types_ import NextFn
from nestipy.ioc import Inject

from app_service import AppService


@Injectable()
class AppMiddleware(NestipyMiddleware):
    service: Inject[AppService]

    async def use(self, req: Request, res: Response, next_fn: NextFn):
        return await next_fn()
