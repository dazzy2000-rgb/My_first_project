from Python_trenning.oop_example.animals_parent_object import AnimalsParentObject


class DogObject(AnimalsParentObject):
    def __init__(self, name, age):
        print(f"Dog {name} object created")
        self.name = name
        self.age = age
    def go_to_sleep(self,time_to_sleep):
        print(f"going to sleep for {time_to_sleep} seconds")
    def make_noise(self):
        print("Hao hao hao")
    # def calculator_distance(self,time,speed):
    #     distance = time * speed
    #     if distance < 10:
    #         print("The animal is lezzy")
    #     else:
    #         print("The animal is ok")
    #
    #     return distance