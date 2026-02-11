from PythonProject.Python_trenning.playwright_example.oop_vehicies.car_object import carobject
from PythonProject.Python_trenning.playwright_example.oop_vehicies.truck_object import Truckobject

car_1 = carobject("Tayota", True)
car_2 = carobject("Mersedes", False)
truck_1 = Truckobject("Volvo", 8)
car_price = car_1.price_calculator(170000, 18)
car_2_price = car_2.price_calculator(170000, 18,"UK")
truck_price = truck_1.price_calculator_for_truck(300000)
assert car_price < truck_price
print("Test end")
price = [100000,200000,300000]
car_2.price_average(price)