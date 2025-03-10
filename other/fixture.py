import pytest


@pytest.fixture
def temp_file():
    print("\nСоздаём временный файл")
    file = open("temp.txt", "w")
    file.write("Hello, pytest!")
    file.close()

    yield "temp.txt"  # Возвращаем путь к файлу в тест

    print("\nУдаляем временный файл")
    import os
    os.remove("temp.txt")


def test_file_reading(temp_file):
    with open(temp_file, "r") as file:
        content = file.read()
    assert content == "Hello, pytest!"
