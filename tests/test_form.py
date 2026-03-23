import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from ui_client import UIClient

# def test_successful_login(driver, get_valid_data):
#     client = UIClient()
#     login_page = client.login_page(driver)
#     username = get_valid_data["username"]
#     password = get_valid_data["password"]
#     dashboard_page = client.login(login_page, username, password)
#     flash = dashboard_page.find_element(By.ID, "flash")
#     assert "You logged into a secure area!" in flash.text
#
#
# def test_unsuccessful_login(driver, invalid_login):
#     client = UIClient()
#     login_page = client.login_page(driver)
#     username, password, expected_message = invalid_login
#     dashboard_page = client.login(login_page, username, password)
#     flash = dashboard_page.find_element(By.ID, "flash")
#     assert expected_message in flash.text
base_url = "https://the-internet.herokuapp.com/login"
valid_data = {
    "username": "tomsmith",
    "password": "SuperSecretPassword!",
}
invalid_data = {
    "username": "Error",
    "password": "Error",
}
massage_error = {
    "username": "Your username is invalid!",
    "password": "Your password is invalid!",
}


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_successful_login(driver):
    driver.get(base_url)
    username_input = driver.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys(valid_data["username"])
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(valid_data["password"])
    button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
    button_login.click()
    flash = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in flash.text


@pytest.mark.parametrize("username, password, expected_massage", [
    (invalid_data["username"], valid_data["password"], massage_error["username"]),
    (valid_data["username"], invalid_data["password"], massage_error["password"]),
])
def test_unsuccessful_login(driver, username, password, expected_massage):
    driver.get(base_url)
    username_input = driver.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)
    button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
    button_login.click()
    flash = driver.find_element(By.ID, "flash")
    assert expected_massage in flash.text
