from appium.webdriver.common.appiumby import AppiumBy
from src.hookers.appHookers import BasePage
import json
class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        with open("locators.json", "r") as file:
            self.locators = json.load("../../src/locators/locators.json")["loginPage"]

    def login(self, username, password):
        USERNAME_FIELD = (AppiumBy.ID, self.locators["username_field"])
        PASSWORD_FIELD = (AppiumBy.ID, self.locators["password_field"])
        LOGIN_BUTTON = (AppiumBy.ID, self.locators["login_button"])

        self.send_keys(USERNAME_FIELD, username)
        self.send_keys(PASSWORD_FIELD, password)
        self.click(LOGIN_BUTTON)
