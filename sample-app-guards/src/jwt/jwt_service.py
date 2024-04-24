from typing import Union

import jwt
from nestipy.common import Injectable
from nestipy_ioc import Inject

from .builder import JWT_OPTION_TOKEN


@Injectable()
class JwtService:
    _options: Inject[JWT_OPTION_TOKEN]

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
