
class Super_hero:

    name = str

    super_powers = str 

    universe = str

    def set_super_hero(self,name,super_powers,universe):

        self.name = name

        self.super_powers = super_powers

        self.universe = universe

    def dispaly_super_hero(self):

        print(self.name,self.super_powers,self.universe)

batman_instance = Super_hero()

batman_instance.set_super_hero("BATMAN","fly,run","dc")

minnal_murali_instance = Super_hero()

minnal_murali_instance.set_super_hero("TOVINO","fly,strength","Basiluniverse")

minnal_murali_instance.dispaly_super_hero()


    