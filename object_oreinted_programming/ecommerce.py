
from abc import ABC,abstractmethod

class Ecommerce(ABC):

    @abstractmethod
    def product_list(self):
        pass

    @abstractmethod
    def add_to_cart(self):
        pass

    @abstractmethod
    def cart_summary(self):
        pass

    @abstractmethod
    def place_order(self):
        pass

class Amazon(Ecommerce):

    def product_list(self):
        print("amazon product list")

    def add_to_cart(self):
        print("amazon add to cart")

    def cart_summary(self):
        print("amazon cart summary")

    def place_order(self):
        print("amazon pace order")

class Flipkart(Ecommerce):

    def product_list(self):
        print("flipkart product list")

    def add_to_cart(self):
        print("flipkart add to cart")

    def cart_summary(self):
        print("flipkart cart summary")

    def place_order(self):
        print("flipkart pace order")

amazon_instance = Amazon()

amazon_instance.place_order()

amazon_instance.cart_summary()

flipkart_instance = Flipkart()

flipkart_instance.product_list()