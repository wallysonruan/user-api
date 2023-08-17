import enum


class UserRolesEnum(enum.Enum):
    user: str = "usr"
    admin: str = 'adm'

    @classmethod
    def is_string_in_enum(cls, text: str) -> bool:
        return text in [role.value for role in UserRolesEnum]

    @classmethod
    def to_string(cls) -> dict:
        return [role.value for role in UserRolesEnum]
