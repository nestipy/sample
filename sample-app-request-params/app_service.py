from nestipy.common import Injectable


@Injectable()
class AppService:

    @classmethod
    async def get(cls):
        return "test"

    @classmethod
    async def post(cls, data: any):
        return "test"

    @classmethod
    async def put(cls, id_: int, data: any):
        return "test"

    @classmethod
    async def delete(cls, id_: int):
        return "test"
