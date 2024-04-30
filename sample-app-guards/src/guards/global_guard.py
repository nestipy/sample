from typing import Union, Awaitable

from nestipy.common import CanActivate
from nestipy.common import Injectable
from nestipy.core import ExecutionContext
from nestipy.ioc import Inject

from ..auth.auth_service import AuthService


@Injectable()
class GlobalGuard(CanActivate):
    auth_service: Inject[AuthService]

    async def can_activate(self, context: ExecutionContext) -> Union[Awaitable[bool], bool]:
        return True
