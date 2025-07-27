import pytest

@pytest.fixture
def connect_to_database():
    connection = "Соединение с базой данных установлено"
    return connection