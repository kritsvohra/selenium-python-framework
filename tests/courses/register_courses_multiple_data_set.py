from pages.courses.register_courses_page import RegisterCoursePage
from utilities.teststatus import StatusResult
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt()
class RegisterCoursesMultipleDataSetTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = StatusResult(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners","123456781234", "1125", "112"), ("Learn Python 3 from scratch", "098765431234", "1122", "321"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll()
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result1, "Enrollment failed verification")
        self.driver.find_element_by_link_text("ALL COURSES").click()