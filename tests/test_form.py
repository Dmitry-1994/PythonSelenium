from selenium.webdriver.common.by import By
from ui_client import UIClient


def test_successful_login(driver, get_valid_data):
    client = UIClient()
    login_page = client.login_page(driver)
    username = get_valid_data["username"]
    password = get_valid_data["password"]
    dashboard_page = client.login(login_page, username, password)
    flash = dashboard_page.find_element(By.ID, "flash-messages")
    assert "You logged into a secure area!" in flash.text


def test_unsuccessful_login(driver, invalid_login):
    client = UIClient()
    login_page = client.login_page(driver)
    username, password, expected_message = invalid_login
    dashboard_page = client.login(login_page, username, password)
    flash = dashboard_page.find_element(By.ID, "flash-messages")
    assert expected_message in flash.text
