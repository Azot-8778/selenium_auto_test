from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def set_up(self):
        self.browser = webdriver.Chrome()

    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        input2.send_keys("uaos@nkld.ck")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        input3.send_keys("wadawd")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        input2.send_keys("uaos@nkld.ck")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        input3.send_keys("wadawd")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайт
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
