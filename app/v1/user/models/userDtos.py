from uuid import UUID

from pydantic import BaseModel, field_validator

from user.models.Enum.userRolesEnum import UserRolesEnum


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
            raise ValueError(f'Role not valid! Valid values: {UserRolesEnum.to_string()}')
        return value


class UserRoleUpdateDtoResponse(BaseModel):
    id: UUID
    role: str

    @field_validator("role")
    def check_if_role_is_valid(cls, value: str):
        if not UserRolesEnum.is_string_in_enum(value):
            raise ValueError(f'Role not valid! Valid values: {UserRolesEnum.to_string()}')
        return value
