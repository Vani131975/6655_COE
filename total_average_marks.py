stu_number = input("Enter student number: ")
name = input("Enter studet name: ")
c_marks = float(input("Enter marks in c: "))
cpp_marks = float(input("Enter marks in cpp: "))
java_marks = float(input("Enter marks in java: "))

total = c_marks + cpp_marks + java_marks
average = total / 3
average = round(average, 2)

if average >= 70:
  result = "Pass"
  if average >= 90:
    grade = "A"
  elif average >= 80:
    grade = "B"
  else:
    grade = "C"
else:
  result = "Fail"
  grade = "None"

print("Student Number is: ", stu_number)
print("Student name is: ", name)
print("Total marks is: ", total)
print("Average score is: ", average)
print("Result is:", result)
print("Grade is: ", grade)
