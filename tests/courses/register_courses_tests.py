from pages.courses.register_courses_page import RegisterCoursePage
from utilities.teststatus import StatusResult
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = StatusResult(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll()
        self.courses.enrollCourse("1234 5678 9012 3456", "1125", "112")
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result1, "Enrollment failed verification")