from Python_trenning.oop_example.cat_object import catObject
from Python_trenning.oop_example.dog_object import DogObject




class mainAnimals():
    dog_1=DogObject("Rexy",4)
    dog_2=DogObject("Lucky",5)
    cat_1=catObject(4,4)

    dog_1.make_noise()
    dog_2.make_noise()
    dog_1.calculator_distance_at_parent(12,10)
    cat_1.make_noise()
    cat_1.calculator_distance_at_parent(5,3)
    dog_1.calculator_distance_at_parent(7,5)