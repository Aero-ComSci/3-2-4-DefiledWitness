from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
computer_sci = Course("Computer Science")
spanish = Course("Spanish")

# TODO: Add two more courses of your choosing

test_student = Student("Jill", "Sample")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bill", "Sample")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)


test_student3 = Student("Billy", "Bob")
test_student3.add_course(spanish)
test_student3.add_course(math)
test_student3.add_course(computer_sci)
test_student3.add_course(history)

Students = [test_student, test_student2, test_student3]

for i in range(len(Students)):
    print(Students[i])
    
for i in range(len(Students)):
    print(f"\n Schedule of {Students[i].get_first_name()} {Students[i].get_last_name()}: \n")
    for course in Students[i].courses:
        print(course)
print("\n \n") #To seperate functions
for student in Students:
    print(student.get_name())

"""
 for this part you may need to review the other skeleton code to:
    - see how to get items from a list
    - see if there is code (like a function) in that file you can call in this file
    - verify that running this file gets you the correct output with information from that file
  Also, review syntax of pulling items from a list from other activities 
"""
