"""This is a file for homework 10."""

import os
import logging
from logging_function import log_event


def clear_log_file():
    """Видаляє лог файл перед тестом."""
    if os.path.exists('login_system.log'):
        os.remove('login_system.log')


def reset_logging():
    """Скидає налаштування логування."""
    logging.getLogger().handlers.clear()


def read_log_file():
    """
    Читає лог файл і повертає його вміст як список рядків.

    Returns:
        list: Список рядків з лог файлу.
    """
    with open('login_system.log', 'r') as log_file:
        return log_file.readlines()


def test_log_event(username, status, expected_level):
    """
    Тестує логування події.

    Args:
        username (str): Ім'я користувача.
        status (str): Статус події.
        expected_level (str): Очікуваний рівень логування.
    """
    clear_log_file()
    reset_logging()
    log_event(username, status)

    log_lines = read_log_file()
    assert len(log_lines) == 1
    last_log = log_lines[0]

    assert expected_level in last_log
    assert f"Login event - Username: {username}, Status: {status}" in last_log


if __name__ == "__main__":
    test_cases = [
        ("test_user_1", "success", "INFO"),
        ("test_user_2", "expired", "WARNING"),
        ("test_user_3", "failed", "ERROR"),
        ("test_user_4", "unknown", "ERROR"),
    ]

    for username, status, expected_level in test_cases:
        test_log_event(username, status, expected_level)
        print(f"Test with username={username} and status={status} passed.")
