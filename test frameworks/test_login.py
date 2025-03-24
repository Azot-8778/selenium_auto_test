from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import pytest
import math
import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    options = Options()
    options.page_load_strategy = 'eager'
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    welcome_text = ""
    numbers = ["895", "896","897","898","899","903","904","905"]

    @pytest.mark.parametrize('links', numbers)
    def test_login_link(self, browser, links, load_config):

        link = f"https://stepik.org/lesson/236{links}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        login = load_config['login_stepik']
        password = load_config['password_stepik']

        browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
        field_login = browser.find_element(By.NAME, "login")
        field_login.send_keys(login)
        field_login = browser.find_element(By.NAME, "password")
        field_login.send_keys(password)
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        time.sleep(5)

        input_graph = browser.find_element(By.TAG_NAME, "textarea")
        answer = str(math.log(int(time.time())))
        input_graph.send_keys(answer)

        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))).click()
        message = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text
        assert message == 'Correct!', f"Should be correct, not {message}"

if __name__ == "__main__":
    unittest.main()







