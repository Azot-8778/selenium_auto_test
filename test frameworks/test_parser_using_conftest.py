from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


# pytest -s -v --browser_name=chrome test_parser_using_conftest.py
# pytest -s -v --browser_name=firefox test_parser_using_conftest.py