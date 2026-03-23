import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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


@pytest.fixture
def get_valid_data():
    return valid_data


@pytest.fixture(params=[
    (invalid_data["username"], valid_data["password"], massage_error["username"]),
    (valid_data["username"], invalid_data["password"], massage_error["password"]),
])
def invalid_login(request):
    return request.param
