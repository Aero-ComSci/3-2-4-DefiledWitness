import pytest
from student import Student
from course import Course

math = Course("Algebra I")
language = Course("Spanish I")

def test_FNLN():
    test_stuFNLN = Student("Tester","Chester")
    assert test_stuFNLN.get_name() == "Tester Chester"

def test_listStudents():
    test_stuList = Student("Tester", "Chester")
    test_stuList.add_course(math)
    test_stuList.add_course(language)
    assert test_stuList.courses[0] == math
    assert len(test_stuList.courses) == 2




