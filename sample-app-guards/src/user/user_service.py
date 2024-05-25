from nestipy.common import Injectable

from .user_dto import UpdateUserDto, CreateUserDto


@Injectable()
class UserService:

    async def list(self):
        return "test"

    async def create(self, data: CreateUserDto):
        return "test"

    async def update(self, id: int, data: UpdateUserDto):
        return "test"

    async def delete(self, id: int):
        return "test"

    async def find_by_email(self, email: str):
        return 'test'

    async def find_by_id(self, id: str):
        return "user"
