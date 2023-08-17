import enum


class UserRolesEnum(enum.Enum):
    user: str = "usr"
    admin: str = "adm"

    @classmethod
    def get_all_roles(cls) -> str:
        roles = [role.value for role in cls]
        roles = roles.__str__()
        roles = roles.replace("[", "(")
        roles = roles.replace("]", ")")
        return roles
