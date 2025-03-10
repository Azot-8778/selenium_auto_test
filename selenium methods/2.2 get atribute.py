import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    treasure = browser.find_element(By.ID, "treasure")
    x_element = treasure.get_attribute("valuex")

    y = calc(x_element)

    input_str = browser.find_element(By.ID, "answer")
    input_str.send_keys(y)

    check_box1 = browser.find_element(By.ID, "robotCheckbox")
    check_box1.click()

    radio_button1 = browser.find_element(By.ID, "robotsRule")
    radio_button1.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()