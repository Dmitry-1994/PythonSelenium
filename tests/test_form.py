import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

base_url = "https://the-internet.herokuapp.com/login"
valid_data = {
    "username": "tomsmith",
    "password": "SuperSecretPassword!",
}
invalid_data = {
    "username": "Error",
    "password": "Error",
}
massage = {
    "valid_data": "You logged into a secure area!",
    "username_error": "Your username is invalid!",
    "password_error": "Your password is invalid!",
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


@pytest.mark.parametrize("username, password, expected_massage", [
    (valid_data["username"], valid_data["password"], massage["valid_data"]),
    (invalid_data["username"], valid_data["password"], massage["username_error"]),
    (valid_data["username"], invalid_data["password"], massage["password_error"]),
])
def test_login(driver, username, password, expected_massage):
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
