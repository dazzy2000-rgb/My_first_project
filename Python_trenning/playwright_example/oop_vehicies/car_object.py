from PythonProject.Python_trenning.playwright_example.oop_vehicies.vehicle_parent import vehicleparent


class carobject(vehicleparent):
    def __init__(self,brand,is_electric):
        self.brand = brand
        self.is_electric = is_electric
    def battary_available(self,capacity,ussage):
        if (self.is_electric==True):
            print ("truing to calculate is available battary")
            remaining_capacity = capacity - ussage
            return remaining_capacity
        else:
            return -1

    def price_average(self, prices):
        for i in prices:
            sum_price: int = 0
            sum_price += i
            average_price =sum_price/len(prices)
            print(f"The average price is {average_price}")
            return average_price