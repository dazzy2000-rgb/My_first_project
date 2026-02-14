from PythonProject.Python_trenning.playwright_example.oop_students.driver_object import Driver
from PythonProject.Python_trenning.playwright_example.oop_students.students_object import Student

student_1 = Student("Leonardo", "Kaktus")
student_2 = Student("Michael", "Kapusta")
driver_1 = Driver("Leo Mich", "a")
student_1.age_parametr(20)
student_2.age_parametr(16)
driver_1.age_parametr(30)
grades_1=[60,45,80,75]
avg_1=student_1.get_avg_grade(grades_1)
grades_2=[35,70.60,85]
avg_2=student_2.get_avg_grade(grades_2)
student_1.is_pass(grades_1)
student_2.is_pass(grades_2)
assert avg_1 > avg_2 , "AVG2 is higher VS AVG1"
print ("AVG1 is higher VS AVG2" )