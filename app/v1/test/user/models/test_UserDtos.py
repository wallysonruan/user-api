import uuid

from app.v1.src.user.models.enums.userRolesEnum import UserRolesEnum
from app.v1.src.user.models.userDtos import UserRoleUpdateDtoResponse, UserRoleUpdateDtoRequest


def test_should_be_sucessfull__valid_role_in_user_role_update_dto_response():
    result: bool = True

    try:
        UserRoleUpdateDtoResponse(id=uuid.uuid4(), role='usr')
        UserRoleUpdateDtoResponse(id=uuid.uuid4(), role='adm')
    except ValueError:
        result = False

    assert result


def test_should_fail__role_not_valid_in_user_role_update_dto_response():
    result: bool = True

    try:
        UserRoleUpdateDtoResponse(id=uuid.uuid4(), role='oi')
    except ValueError:
        result = False

    assert not result


def test_should_return_error_message_upon_role_validation_in_user_role_update_dto_response():
    result: bool = True
    message: str = f'Role not valid! Valid values: {UserRolesEnum.to_string()}'

    try:
        UserRoleUpdateDtoResponse(id=uuid.uuid4(), role='oi')
    except ValueError as exception:
        if exception.__str__().__contains__(message):
            result = False

    assert not result


def test_should_fail__id_invalid_format_in_user_role_update_dto_response():
    result: bool = True

    try:
        UserRoleUpdateDtoResponse(id="a", role='usr')
    except ValueError as e:
        result = False

    assert not result


def test_should_be_sucessfull__id_valid_format_in_user_role_update_dto_response():
    result: bool = True

    try:
        UserRoleUpdateDtoResponse(id=uuid.uuid4(), role='usr')
    except ValueError as e:
        result = False

    assert result


def test_should_be_sucessfull__valid_role_in_user_role_update_dto_request():
    result: bool = True

    try:
        UserRoleUpdateDtoRequest(id=uuid.uuid4(), role='usr')
        UserRoleUpdateDtoRequest(id=uuid.uuid4(), role='adm')
    except ValueError:
        result = False

    assert result


def test_should_fail__role_not_valid_in_user_role_update_dto_request():
    result: bool = True

    try:
        UserRoleUpdateDtoRequest(id=uuid.uuid4(), role='oi')
    except ValueError:
        result = False

    assert not result


def test_should_return_error_message_upon_role_validation_in_user_role_update_dto_request():
    result: bool = True
    message: str = f'Role not valid! Valid values: {UserRolesEnum.to_string()}'

    try:
        UserRoleUpdateDtoRequest(id=uuid.uuid4(), role='oi')
    except ValueError as exception:
        if exception.__str__().__contains__(message):
            result = False

    assert not result


def test_should_fail__id_invalid_format_in_user_role_update_dto_request():
    result: bool = True

    try:
        UserRoleUpdateDtoRequest(id="a", role='usr')
    except ValueError as e:
        result = False

    assert not result


def test_should_be_sucessfull__id_valid_format_in_user_role_update_dto_request():
    result: bool = True

    try:
        UserRoleUpdateDtoRequest(id=uuid.uuid4(), role='usr')
    except ValueError as e:
        result = False

    assert not result
