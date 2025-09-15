
class GrandParent:

    def house(self):

        print("grandparent house")

class Parent(GrandParent):

    def bike(self):

        print("parent bike")

class Child(Parent):

    def car(self):

        print("child car")

child_instamce = Child()

child_instamce.car()

child_instamce.bike()

child_instamce.house()
