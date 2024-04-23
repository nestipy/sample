from nestipy.common import Request, Response
from nestipy.common.middleware import NestipyMiddleware
from nestipy.types_ import NextFn
from nestipy_decorator import Injectable


@Injectable()
class UserMiddleware(NestipyMiddleware):
    async def use(self, req: Request, res: Response, next_fn: NextFn):
        return await next_fn()


async def user_middleware(req: Request, res: Response, next_fn: NextFn):
    return await next_fn()
