import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class RegisterCoursePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "input#search"
    _click_search_icon = "//i[@class='fa fa-search']"
    _course = "//h4[@class='dynamic-heading']"
    #_enroll_button = "[data-uniqid='1595290194536']"
    _enroll_button = "//button[.='Enroll in Course']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _country_name = "//select[@name='country-list']"
    _submit_enroll = "//div[@class='col-xs-12']/button[1]"
    _enroll_error_message = "//span[.='Your card number is invalid.']"

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, locatorType="css")
        self.elementClick(self._click_search_icon, locatorType="xpath")

    def selectCourseToEnroll(self):
        self.elementClick(self._course, locatorType="xpath")

    def clickEnrollButton(self):
        self.elementClick(self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        # This particular frame takes atleast 6 seconds to show
        time.sleep(10)
        # self.switchToFrame(name="__privateStripeFrame1205")
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.sendKeys(num, self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame1207")
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(exp, self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame1206")
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cvv, self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickEnrollButton()
        self.webScroll("down")
        time.sleep(10)
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
