from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "SIGN IN"
    _email_field = "[role='form'] #email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"
    _logout = "Logout"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="css")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']/img", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        time.sleep(5)
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try again.')]",
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field, locatorType="css")
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field, locatorType="id")
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")

    def logOut(self):
        self.nav.navigateToUserSettingsIcon()
        logOutLinkElement = self.waitForElement(locator=self._logout, locatorType="link", pollFrequency=1)
        self.elementClick(element=logOutLinkElement)