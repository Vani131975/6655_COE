class Student:
  student_id = ""
  student_name = ""
  student_class = None

  def display(self):
    print("Original attributes and their values of the student classs: ")
    print("Student ID: ", self.student_id)
    print("Student Name: ", self.student_name)
    if self.student_class:
      print("Student Class: ", self.student_class)


student = Student()
student.student_id = input("Enter Student Id: ")
student.student_name = input("Enter Student Name: ")
student.display()
