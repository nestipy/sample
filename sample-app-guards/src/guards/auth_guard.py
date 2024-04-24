from typing import Union, Awaitable

from nestipy.common import CanActivate
from nestipy.common import HttpStatus, HttpStatusMessages, HttpException
from nestipy.common import Injectable
from nestipy.core import ExecutionContext
from nestipy_ioc import Inject

from ..jwt.jwt_service import JwtService
from ..user.user_service import UserService


@Injectable()
class AuthGuard(CanActivate):
    user_service: Inject[UserService]
    jwt_service: Inject[JwtService]

    async def can_activate(self, context: ExecutionContext) -> Union[Awaitable[bool], bool]:
        req = context.switch_to_http().get_request()
        authorization: str = req.headers.get('authorization')
        try:
            payload = await self.jwt_service.decode(authorization.replace('Bearer ', ''))
        except Exception as e:
            raise HttpException(HttpStatus.UNAUTHORIZED, HttpStatusMessages.UNAUTHORIZED)
        user_id = payload['sub']
        req.user = await self.user_service.find_by_id(user_id)
        return True
