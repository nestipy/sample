from typing import Union, Awaitable

from nestipy.common import CanActivate
from nestipy.core.context.execution_context import ExecutionContext
from nestipy_cli.templates.project.app_service import AppService
from nestipy_decorator import Injectable
from nestipy_ioc import Inject


@Injectable()
class GlobalGuard(CanActivate):
    app_service: Inject[AppService]

    async def can_activate(self, context: ExecutionContext) -> Union[Awaitable[bool], bool]:
        return True
