from PythonProject.Python_trenning.playwright_example.oop_vehicies.vehicle_parent import vehicleparent


class Truckobject(vehicleparent):
    def __init__(self,brand,whells_amount):
        self.brand = brand
        self.whells_amount = whells_amount
    def calculate_distance(self,time,speed):
        distance = speed*time
        return distance

    def price_calculator_for_truck(self, price):
        total_price = price * 1.10
        print(f"The total price is {total_price}")
        return total_price