"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configuration

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        :param browser:
        returns none
        """
        self.browser = browser

    def getWebDriverInstance(self):
        """
        get WebDriver Instance based on the browser configuration

        :return:
            'WebDriver Instance'
        """
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == "iexplorer":
            # Set IE driver
            driver = webdriver.Ie(executable_path="D:\selenium tutorials\selenium2\drivers\IEDriverServer.exe")
        elif self.browser == "firefox":
            # Set Firefox driver
            driver = webdriver.Firefox(executable_path="D:\selenium tutorials\selenium2\drivers\geckodriver.exe")
        elif self.browser == "chrome":
            # Set Chrome driver
            driver = webdriver.Chrome(executable_path="D:\selenium tutorials\selenium2\drivers\chromedriver")
        else:
            # Set Chrome driver
            driver = webdriver.Chrome(executable_path="D:\selenium tutorials\selenium2\drivers\chromedriver")
        # Setting driver implicit timeout for an element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading the browser with App URL
        driver.get(baseURL)
        return driver
