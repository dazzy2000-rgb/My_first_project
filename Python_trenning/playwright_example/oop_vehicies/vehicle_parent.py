from statistics import quantiles


class vehicleparent():
    def price_calculator(self,price,tax,country_cod="IL"):
        total_price = price*(100+tax)/100
        print(f"The total price is {total_price}")
        print(f"country cod={country_cod}")
        return total_price

