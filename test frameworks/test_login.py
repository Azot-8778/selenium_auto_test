from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import pytest
import math


answer = math.log(int(time.time()))

@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('data.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    welcome_text = ""
    numbers = ["95", "96","97","98","99","03","04","05"]

    @pytest.mark.parametrize('links', numbers)
    def test_login_link(self, browser, links, load_config):

        link = f"https://stepik.org/lesson/2368{links}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        login = load_config['login_stepik']
        password = load_config['password_stepik']

        enter_button = browser.find_element(By.ID, "ember466").click()
        time.sleep(10)
        field_login = browser.find_element(By.NAME, "login")
        field_login.send_keys(login)
        field_login = browser.find_element(By.NAME, "password")
        field_login.send_keys(password)
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()






