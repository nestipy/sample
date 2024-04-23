from nestipy.common import Request, Response
from nestipy.common.middleware import NestipyMiddleware
from nestipy.types_ import NextFn
from nestipy_decorator import Injectable
from nestipy_ioc import Inject

from app_service import AppService


@Injectable()
class AppMiddleware(NestipyMiddleware):
    service: Inject[AppService]

    async def use(self, req: Request, res: Response, next_fn: NextFn):
        return await next_fn()
