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
massage_error = {
    "username": "Your username is invalid!",
    "password": "Your password is invalid!",
}


@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def valid_login(driver):
    driver.get(base_url)
    username_input = driver.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys(valid_data["username"])

    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(valid_data["password"])

    button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
    button_login.click()
    yield driver

@pytest.fixture
def login_page(driver):
    driver.get(base_url)
    yield driver

@pytest.fixture(params=[
    (invalid_data["username"], valid_data["password"], massage_error["username"]),
    (valid_data["username"], invalid_data["password"], massage_error["password"]),
])
def invalid_login(driver, request):
    return request.param