from Python_trenning.oop_example.animals_parent_object import AnimalsParentObject


class catObject(AnimalsParentObject):
    def __init__(self, legs_amount, age):
        self.legs_amount = legs_amount
        self.age = age

    def make_noise(self):
         print("Miao miao miao")

    # def calculator_distance(self,time,speed):
    #     distance = time * speed
    #     if distance < 10:
    #         print("The animal is lezzy")
    #     else:
    #         print("The animal is ok")
