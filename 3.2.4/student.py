from course import Course

class Student:
    
    student_id = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
    def __str__(self):
        
        course_list = []
        for course in self.courses:
            course_list += "\n\t" + str(course)
        return f"student ID: {self.student_id} and Name: {self.first_name} {self.last_name} and Courses:{course_list}"
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name
        
    def get_student_id(self):
        return self.student_id
    
    def add_course(self, new_course):
        self.courses.append(new_course)
        #print ("Complete this based on what the program is doing here.")