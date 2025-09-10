
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