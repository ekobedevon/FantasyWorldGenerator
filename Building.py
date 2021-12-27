from random import choice, randint
import NPC
import Generator


class Building():
    building_type = ""
    building_name = ""
    owner = None
    occupants = []
    hooks = []
    def __init__(self,gen: Generator.generator = None,dict_data = None):
        self.owner = NPC.NPC(gen=gen)
        if dict_data == None:
            building_name, building_owner, building_type = gen.generateBuilding()
            self.building_type = building_type
            self.building_name = building_name
            if building_owner != "": #if the building is not a house
                self.owner.profession = building_owner
            
            for x in range(0,randint(0,4)): # generate some npcs for the building
                temp_npc = NPC.NPC(gen=gen)
                self.occupants.append(temp_npc)

            for x in range(0,randint(0,2)):
                hook= None
                match(randint(0,3)):
                    case 0:
                        hook = gen.generateHook(self.owner.name) # generate a quest given by the building owner
                    case 1:
                        npc_occupant = choice(self.occupants)
                        name = npc_occupant.name # get the name of the occupant
                        hook = gen.generateHook(name)
                    case 2:
                        hook ="On the Quest Board: " + gen.generateHook(Q_type=1)
                    case 3:
                        hook =gen.generateHook(Q_type=0)
                self.hooks.append(hook)
                    
                    
            

    def __dict__(self):
        building_dict = {}
        building_dict["building_type"] = self.building_type
        building_dict["building_name"] = self.building_name
        building_dict["owner"] = self.owner.__dict__
        building_dict["occupants"] = {}
        for person in self.occupants:
            
            building_dict["occupants"][person.name] = person.__dict__
        building_dict["hooks"] = self.hooks

        return building_dict

         