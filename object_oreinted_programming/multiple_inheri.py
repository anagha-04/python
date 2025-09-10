
class Father:

    def cricket_skill(self):

        print("father cricket skill")

class Mother():


    def cooking_skill(self):

        print("mother cooking skill")

class Child(Father,Mother):

    def learning_skill(self):

        print("child learning skill")

child_instance = Child()

child_instance.cooking_skill()

child_instance.cricket_skill()

