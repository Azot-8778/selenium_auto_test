import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, "book")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), "$100")
    )

    button.click()


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    input = calc(x)

    input_str = browser.find_element(By.ID, "answer")
    input_str.send_keys(input)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()