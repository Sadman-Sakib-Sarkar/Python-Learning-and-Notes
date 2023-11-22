# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price
    
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     price = property(get_price, set_price) #This is called property here we pass the references only

# product = Product(10)
# print(product.price)
# product.price = -5
# print(product.price)


#We can achieve the same thing using properties:

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(10)
print(product.price)
product.price = -5
print(product.price)