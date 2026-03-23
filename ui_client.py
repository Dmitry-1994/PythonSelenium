from selenium.webdriver.common.by import By


class UIClient:
    base_url = "https://the-internet.herokuapp.com/login"

    def login_page(self, driver):
        driver.get(self.base_url)
        return driver

    def login(self, driver, username, password):
        username_input = driver.find_element(By.ID, "username")
        username_input.clear()
        username_input.send_keys(username)

        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys(password)

        button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
        button_login.click()
        return driver
