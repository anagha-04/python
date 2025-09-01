

class Book:

    name: str

    author: str

    price: int

    def __init__(self,name,author,price):

      self.name = name

      self.author = author

      self.price = price

    def dispaly_book(self):
       
       print(self.name,self.author,self.price)

    def __str__(self):
       
       return self.name

book_instance = Book("goatlife","benyamin",600)

book_instance.dispaly_book()

print(book_instance)







