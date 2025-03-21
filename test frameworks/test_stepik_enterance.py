from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import pytest
import math

link = "https://stepik.org/lesson/236895/step/1?auth=login"
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
    def test_authorization(self, browser, load_config):
        browser.get(link)
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        browser.implicitly_wait(5)

        field_login = browser.find_element(By.NAME, "login")
        field_login.send_keys(login)
        field_login = browser.find_element(By.NAME, "password")
        field_login.send_keys(password)
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        time.sleep(5)

        input_graph = browser.find_element(By.ID, "ember532")
        input_graph.send_keys(str(answer))
        button_send = browser.find_element(By.CLASS_NAME, "submit-submission")
        button_send.click()
        time.sleep(10)
        self.welcome_text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text

    def test_check(self, welcome_text):
        assert welcome_text == 'Correct!', f"Should be correct? not {welcome_text}"


if __name__ == "__main__":

    unittest.main()






