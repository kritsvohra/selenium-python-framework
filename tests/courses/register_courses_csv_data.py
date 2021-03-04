from pages.courses.register_courses_page import RegisterCoursePage
from utilities.teststatus import StatusResult
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt()
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = StatusResult(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:/selenium tutorials/letskodeit3/test_data.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        time.sleep(1)
        self.courses.selectCourseToEnroll()
        time.sleep(1)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(1)
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result1, "Enrollment failed verification")