from typing import Any

from nestipy.common import ExceptionFilter, Catch, HttpException
from nestipy.core import ArgumentHost


@Catch()
class HttpExceptionFilter(ExceptionFilter):
    async def catch(self, exception: HttpException, host: ArgumentHost) -> Any:
        res = host.get_response()
        return await res.status(exception.status_code).json({
            'error': exception.status_code,
            'message': exception.message
        })
        # print('Catcher')
