from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CreateUser:
    user_id: int
    username: str
    first_name: str
    last_name: str
    middle_name: str | None
