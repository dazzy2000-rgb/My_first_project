

class AnimalsParentObject():
    def calculator_distance_at_parent(self, time, speed):
        distance = time * speed
        if distance < 10:
            print("The animal is lezzy")
        else:
            print("The animal is ok")