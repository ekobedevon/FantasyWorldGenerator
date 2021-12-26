import NPC
import Generator


class Building():
    name = ""
    building_type = ""
    owner = NPC.NPC()
    def __init__(self,gen: Generator.generator = None,dict_data = None):
        if dict_data == None:
            pass
        pass