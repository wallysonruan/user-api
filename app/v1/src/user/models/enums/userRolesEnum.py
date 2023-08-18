import enum
from typing import List, Callable, Any


class UserRolesEnum(enum.Enum):
    user: str = "usr"
    admin: str = 'adm'

    @classmethod
    def is_string_in_enum(cls, text: str) -> bool:
        return text in [role.value for role in UserRolesEnum]

    @classmethod
    def to_string(cls) -> list[Callable[[], Any]]:
        return [role.value for role in UserRolesEnum]
