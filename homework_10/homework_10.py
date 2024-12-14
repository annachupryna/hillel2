"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


def test_log_event_success():

    username, status = 'Ooolena', 'success'
    log_event(username, status)
    with open('login_system.log', 'r') as log_file:
        last_log = log_file.readlines()[-1]

    expected_result = f"Login event - Username: {username}, Status: {status}"
    assert expected_result in last_log


def test_log_event_expired():
    username, status = 'Vadym', 'expired'
    log_event(username, status)
    with open('login_system.log', 'r') as log_file:
        last_log = log_file.readlines()[-1]

    expected_result = f"Login event - Username: {username}, Status: {status}"
    assert expected_result in last_log


def test_log_event_failed():
    username, status = 'Serhii', 'failed'
    log_event(username, status)
    with open('login_system.log', 'r') as log_file:
        last_log = log_file.readlines()[-1]

    expected_result = f"Login event - Username: {username}, Status: {status}"
    assert expected_result in last_log
