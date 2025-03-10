import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(By.ID, "num1")
    x_element = num1.text

    num2 = browser.find_element(By.ID, "num2")
    y_element = num2.text

    suma = str(int(x_element) + int(y_element))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(suma)  # ищем элемент с текстом "Python"

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()