from typing import List, Callable, Any

from v1.src.user.models.enums.userRolesEnum import UserRolesEnum


def test_should_return_true():
    result: bool = UserRolesEnum.is_string_in_enum('usr')
    assert result


def test_should_return_false():
    result: bool = UserRolesEnum.is_string_in_enum('test')
    assert not result


def test_should_return_expected_values_sucessfully():
    expected_roles: List[str] = ["usr", "adm"]
    returned: List[Callable[[], Any]] = UserRolesEnum.to_string()

    assert expected_roles.__eq__(returned)


def test_should_fail_to_return_expected_values_even_with_some_correct_values():
    expected_roles: List[str] = ["usr", "adm", "aa"]
    returned: List[Callable[[], Any]] = UserRolesEnum.to_string()

    assert not expected_roles.__eq__(returned)


def test_should_failt_to_return_expected_values_all_different():
    expected_roles: List[str] = ["user", "admirer", "aa"]
    returned: List[Callable[[], Any]] = UserRolesEnum.to_string()

    assert not expected_roles.__eq__(returned)
