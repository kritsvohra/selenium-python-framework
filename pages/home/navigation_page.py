from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "MY COURSES"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _home = "HOME"
    _user_settings_icon = "//button[@id='dropdownMenu1']/img"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="link")

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="link")

    def navigateToUserSettingsIcon(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)