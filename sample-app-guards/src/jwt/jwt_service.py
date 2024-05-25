from typing import Union, Annotated

import jwt
from nestipy.common import Injectable
from nestipy.ioc import Inject

from .builder import JWT_OPTION_TOKEN, JwtOption


@Injectable()
class JwtService:
    _options: Annotated[JwtOption, Inject(JWT_OPTION_TOKEN)]

    async def decode(self, token: str):
        return jwt.decode(
            token,
            key=self._options.secret,
            algorithms=self._options.algorithms
        )

    async def sign(self, payload: Union[str, int, dict, list, set]):
        payload = {
            'exp': self._options.exp,
            'sub': payload
        }
        return jwt.encode(
            payload,
            key=self._options.secret,
        )
