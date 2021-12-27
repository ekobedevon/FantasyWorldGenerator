import NPC
import Generator


class Building():
    building_type = ""
    building_name = ""
    owner = None
    def __init__(self,gen: Generator.generator = None,dict_data = None):
        self.owner = NPC.NPC(gen=gen)
        if dict_data == None:
            building_name, building_owner, building_type = gen.generateBuilding()
            self.building_type = building_type
            self.building_name = building_name
            if building_owner != "":
                self.owner.profession = building_owner

    def __dict__(self):
        building_dict = {}
        building_dict["building_type"] = self.building_type
        building_dict["building_name"] = self.building_name
        building_dict["owner"] = self.owner.__dict__
        return building_dict
         