
#single inheritance
#one child class acquring methods and attributes from one parent class



class Parent:

    def car(self):

        print("parent swit car")

    def bike(self):

        print("parent passion pro")

class child(Parent):


    def bike(self):

        print("child triumph bike")

child_instance = child()

child_instance.bike()

child_instance.car()