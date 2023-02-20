import Student
import Grades

p1 = Student.Student("Justin Pulga", 21)
p2 = Grades.Grades("CPE028", 3, 95)

print("Name: " + p1.name)
print("Age: " + str(p1.age))
print("Course Code: ", p2.Course_Code)
print("Course Unit: ", p2.Course_Units)
print("Course Grade: ", p2.Course_Grade)