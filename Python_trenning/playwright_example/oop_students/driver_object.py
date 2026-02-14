from PythonProject.Python_trenning.playwright_example.oop_students.person_parent import personparent


class Driver(personparent):
    def __init__(self,name:str,license:str):
        self.name = name
        self.license = license

    def get_vehicles_vs_licenses(self):
        if self.license=="a":
            print(f"you allowed to use motorcycle only")
        elif self.license=="b":
            print(f"you allowed to use car and motorcycle")
        elif self.license=="c":
            print(f"you allowed to use truck")
        else:
            print(f"yous license did not recognised")
