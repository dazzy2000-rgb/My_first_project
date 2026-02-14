from PythonProject.Python_trenning.playwright_example.oop_students.person_parent import personparent


class Student(personparent):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_avg_grade(self, grades: list) ->float:
        summery = 0
        for grade in grades:
            summery += grade
        avg = summery // len(grades)
        return avg

    def is_pass(self, grades: list, ref_value: int = 60) -> bool:
        summery = 0
        for grade in grades:
            summery += grade
            self.avg = summery // len(grades)

            print(f"The average grade of {self.first_name} {self.last_name}  is {self.avg}")
            if self.avg > ref_value:
                return True
            else:
                return False

    def print_avg(self):
        print(f"The average grade of is {self.avg}")



