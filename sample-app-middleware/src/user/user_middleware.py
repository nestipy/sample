from nestipy.common import Injectable
from nestipy.common import NestipyMiddleware
from nestipy.common import Request, Response
from nestipy.types_ import NextFn


@Injectable()
class UserMiddleware(NestipyMiddleware):
    async def use(self, req: Request, res: Response, next_fn: NextFn):
        return await next_fn()


async def user_middleware(req: Request, res: Response, next_fn: NextFn):
    return await next_fn()
