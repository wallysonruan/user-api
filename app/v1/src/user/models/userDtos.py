from uuid import UUID

from pydantic import BaseModel, field_validator

from v1.src.user.models.enums.userRolesEnum import UserRolesEnum

ROLE_ERROR_VALIDATION_MESSAGE: str = f'Role not valid! Valid values: {UserRolesEnum.to_string()}'


class UserDtoResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str


class UserDtoRequest(BaseModel):
    first_name: str
    last_name: str


class UserRoleUpdateDtoRequest(BaseModel):
    id: UUID
    role: str

    @field_validator("role")
    def check_if_role_is_valid(cls, value: str):
        if not UserRolesEnum.is_string_in_enum(value):
            raise ValueError(ROLE_ERROR_VALIDATION_MESSAGE)
        return value


class UserRoleUpdateDtoResponse(BaseModel):
    id: UUID
    role: str

    @field_validator("role")
    def check_if_role_is_valid(cls, value: str):
        if not UserRolesEnum.is_string_in_enum(value):
            raise ValueError(ROLE_ERROR_VALIDATION_MESSAGE)
        return value
