import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

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