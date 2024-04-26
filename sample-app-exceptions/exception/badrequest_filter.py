import datetime
from typing import Any

from nestipy.common import ExceptionFilter, Catch, HttpStatus, HttpStatusMessages, HttpException
from nestipy.core import ArgumentHost


class BadRequestException(HttpException):
    def __init__(self):
        super().__init__(HttpStatus.BAD_REQUEST, HttpStatusMessages.BAD_REQUEST)


@Catch(BadRequestException)
class BadRequestExceptionFilter(ExceptionFilter):
    async def catch(self, exception: HttpException, host: ArgumentHost) -> Any:
        response = host.get_response()
        request = host.get_request()
        status = exception.status_code
        print('Catcher')
        return await response.status(status).json({
            'statusCode': status,
            'timestamp': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            'path': request.path,
            'error': exception.message
        })
