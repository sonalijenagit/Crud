#A class should have only one responsibility and no more
from unicodedata import name


class Books():
   def __init__(self):
       self.book ={}
       self.number = 0
   def add_book(self,book):
       self.number +=1
       self.book[self.number] = book
   def __str__(self):
       return str(self.book)   
b=Books()
b.add_book("A")
b.add_book("B")
b.add_book("c")
print(f"print all books:{b}")
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

a= Student("Ankt",22)
print(a.name)
print(a.age)


