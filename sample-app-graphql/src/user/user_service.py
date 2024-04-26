from nestipy.common import Injectable

from .user_input import UserInput


@Injectable()
class UserService:

    async def list(self) -> str:
        return "test"

    async def create(self, data: UserInput) -> str:
        return "test"