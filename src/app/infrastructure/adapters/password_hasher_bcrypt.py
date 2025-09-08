import base64
import hashlib
import hmac
from typing import NewType

import bcrypt

from app.domain.ports.password_hasher import PasswordHasher
from app.domain.value_objects.raw_password import RawPassword

PasswordPepper = NewType("PasswordPepper", str)


class BcryptPasswordHasher(PasswordHasher):
    def __init__(self, pepper: PasswordPepper):
        self._pepper = pepper

    def hash(self, raw_password: RawPassword) -> bytes:
        base64_hmac_password = self._add_pepper(raw_password, self._pepper)
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(base64_hmac_password, salt)

    @staticmethod
    def _add_pepper(
            raw_password: RawPassword,
            pepper: PasswordPepper,
    ) -> bytes:
        hmac_password = hmac.new(
            key=pepper.encode(),
            msg=raw_password.value.encode(),
            digestmod=hashlib.sha256,
        ).digest()
        return base64.b64encode(hmac_password)

    def verify(
            self,
            raw_password: RawPassword,
            hashed_password: bytes,
    ) -> bool:
        base64_hmac_password = self._add_pepper(raw_password, self._pepper)
        return bcrypt.checkpw(base64_hmac_password, hashed_password)
