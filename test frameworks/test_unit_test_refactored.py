from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestUniqueSelectors(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, link):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys('Dorogov')
        browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys('sawed@gmail.com')
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        return welcome_text

    def test_registration_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
