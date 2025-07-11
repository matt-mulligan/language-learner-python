from unittest.mock import Mock
import getpass

from language_learner.ex01_hello_world import hello


def test_hello__no_name_prints_user(monkeypatch):
    print_mock = Mock()
    monkeypatch.setattr("builtins.print", print_mock)

    hello()

    print_mock.assert_called_once_with(f"Hello {getpass.getuser()}")


def test_hello__given_name_prints(monkeypatch):
    print_mock = Mock()
    monkeypatch.setattr("builtins.print", print_mock)

    hello("billy")

    print_mock.assert_called_once_with("Hello billy")
