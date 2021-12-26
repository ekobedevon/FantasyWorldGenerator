import NPC


class Building():
    name = ""
    building_type = ""
    owner = NPC.NPC()
    def __init__(self,gen: NPC.Generator.generator = None,dict_data = None):
        if dict_data == None:
            pass
        pass