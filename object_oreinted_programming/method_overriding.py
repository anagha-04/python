
"""
"  METHOD OVERRIDING"

customize behaviour in child class without chaninging parent class

to provide specific implimentation of a method that is alredy  defined in parent class
"""
class Parent:

    def home(self):

        print("parent home method")

    def vehicle(self):

        print("parent passion-pro vehicle")

class Child(Parent):

    def vehicle(self):
        
        print("child duke method")

child_instance = Child()

child_instance.vehicle()

child_instance.home()