from user.models.enums.userRolesEnum import UserRolesEnum


def test_should_return_true():
    result: bool = UserRolesEnum.is_string_in_enum('usr')
    assert result
