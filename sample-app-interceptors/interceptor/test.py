from nestipy.common import Injectable
from nestipy.common import NestipyInterceptor
from nestipy.core import ExecutionContext
from nestipy.types_ import NextFn


@Injectable()
class TestInterceptor(NestipyInterceptor):
    async def intercept(self, context: ExecutionContext, next_fn: NextFn):
        print('Intercepted...')
        return await next_fn()
