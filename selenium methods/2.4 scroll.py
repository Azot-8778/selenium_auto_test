import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    input = calc(x)



    input_str = browser.find_element(By.ID, "answer")
    input_str.send_keys(input)

    check_box1 = browser.find_element(By.ID, "robotCheckbox")
    check_box1.click()


    radio_button1 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button1)
    radio_button1.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()