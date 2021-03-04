"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import logging
import random
import string
import traceback
import utilities.custom_logger as cl
import time

class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for specific amount of time
        :param sec:
        :param info:
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
            try:
                time.sleep(sec)
            except InterruptedError:
                traceback.print_stack()

    def getAlphaNumeric(self, length, type="letters"):
        """
        get random string of characters
        :param length: Length of string, number of characters string should have
        :param type: Type of characters string should have. Default is letters
        Provides lower/upper/digits for sifferent types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount = 10):
        """
        Get a unique name
        :param charCount:
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize = 5, itemLength = None):
        """
        Gets a list of valid names
        :param listSize: Number of names. Default is 5 email in a list
        :param itemLength: It should be a list containing number of items equal to listSize
                            This determines length of each item in a list
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        :param actualText: Actual Text
        :param expectedText: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: "+actualText)
        self.log.info("Expected Text From Application Web UI --> :: "+expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match

        :param actualText:
        :param expectedText:
        """
        self.log.info("Actual Text From Application Web UI --> :: "+actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches
        :param expectedList: Expected List
        :param actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        :param expectedList: Expected List
        :param actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True
