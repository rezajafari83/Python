class Computer:
    def __init__(self):
        self.__maxPrice = 900
    
    def sell(self):
        print("Selling price: {}".format(self.__maxPrice))

    def setMaxPrice(self, price):
        self.__maxPrice = price

cmp = Computer()
cmp.sell()

#Change the price(We can't change this attribute because it's private in python)
cmp.__maxPrice = 1000
cmp.sell()

#Using setter function(To change the attribute we must use a setter function)
cmp.setMaxPrice(1000)
cmp.sell()