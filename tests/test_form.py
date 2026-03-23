from asyncio import wait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_successful_login(valid_login):
    # driver.get("https://the-internet.herokuapp.com/login")

    # username_input = driver.find_element(By.ID, "username")
    # username_input.clear()
    # username_input.send_keys("tomsmith")
    #
    # password_input = driver.find_element(By.ID, "password")
    # password_input.clear()
    # password_input.send_keys("SuperSecretPassword!")
    #
    # button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
    # button_login.click()
    driver = valid_login

    flash = driver.find_element(By.ID, "flash-messages")
    assert "You logged into a secure area!" in flash.text
    header = driver.find_element(By.TAG_NAME, "h2")
    assert "Secure Area" in header.text

# def test_unsuccessful_login_name(driver):
#     driver.get("https://the-internet.herokuapp.com/login")
#
#     username_input = driver.find_element(By.ID, "username")
#     username_input.clear()
#     username_input.send_keys("Error")
#
#     password_input = driver.find_element(By.ID, "password")
#     password_input.clear()
#     password_input.send_keys("SuperSecretPassword!")
#
#     button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
#     button_login.click()
#
#     flash = driver.find_element(By.ID, "flash-messages")
#     assert "Your username is invalid!" in flash.text
#
# def test_unsuccessful_login_password(driver):
#     driver.get("https://the-internet.herokuapp.com/login")
#
#     username_input = driver.find_element(By.ID, "username")
#     username_input.clear()
#     username_input.send_keys("tomsmith")
#
#     password_input = driver.find_element(By.ID, "password")
#     password_input.clear()
#     password_input.send_keys("Error")
#
#     button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
#     button_login.click()
#
#     flash = driver.find_element(By.ID, "flash-messages")
#     assert "Your password is invalid!" in flash.text

def test_unsuccessful_login(login_page, invalid_login):
    driver = login_page
    username, password, expected_message = invalid_login
    username_input = driver.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)

    button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
    button_login.click()
    flash = driver.find_element(By.ID, "flash-messages")
    assert expected_message in flash.text