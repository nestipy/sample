from nestipy_decorator import Injectable

from .user_dto import CreateUserDto, UpdateUserDto


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
