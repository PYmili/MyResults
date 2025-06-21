from datetime import datetime, timedelta
from typing import Union

import jwt

from MyResults.settings import SECRET_KEY


class JwtUtil:
    @staticmethod
    def generate_jwt_token(payload: dict) -> str:
        """
        生成jwt
        :param payload: 载荷
        :return: str
        """
        payload['exp'] = datetime.now() + timedelta(hours=1)
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    @staticmethod
    def verify_jwt_token(token: str) -> Union[dict, None]:
        """
        验证jwt
        :param token: 需要验证token
        :return: dict
        """
        try:
            # 验证 JWT
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
