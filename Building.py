from random import choice, randint
from typing import List
import NPC
import Generator
import PySimpleGUI as sg
npc_button_size = (24,3)


class Building():
    building_type = ""
    building_name = ""
    owner = NPC.NPC
    occupants:List[NPC.NPC] = []
    hooks = []
    def __init__(self,gen: Generator.generator = None,dict_data = None,Location:str = ""):
        self.owner =None
        self.owner = NPC.NPC(gen=gen)
        if dict_data == None:
            building_name, building_owner, building_type = gen.generateBuilding(location=Location)
            self.building_type = building_type
            self.building_name = building_name
            if building_owner != "": #if the building is not a house
                self.owner.profession = building_owner
            if self.building_type == "Normal_Homes":
                self.building_name += " of " + self.owner.name
            elif self.building_type == "Notable_Housing":
                self.building_name = gen.generateInterstingName(self.owner.name,self.building_name)    


            self.occupants = []
            for x in range(0,randint(0,4)): # generate some npcs for the building
                temp_npc = NPC.NPC(gen=gen)
                self.occupants.append(temp_npc)
            self.hooks = []
            for x in range(0,randint(0,2)):
                hook= None
                match(randint(0,3)):
                    case 0:
                        hook = gen.generateHook(self.owner.name) # generate a quest given by the building owner
                    case 1:
                        if(len(self.occupants) != 0): # if theri are no occupants besides the owner
                            npc_occupant = choice(self.occupants)
                            name = npc_occupant.name # get the name of the occupant
                            hook = gen.generateHook(name)
                        else:
                            hook ="On the nearby Quest Board: " + gen.generateHook(Q_type=1)
                    case 2:
                        hook ="On the nearby Quest Board: " + gen.generateHook(Q_type=1)
                    case 3:
                        hook =gen.generateHook(Q_type=0)
                self.hooks.append(hook)
            self.occupants.insert(0,self.owner)
                    
                    
            

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
    
    def createDisplay(self):
        layout = [[]]
        colTitle = [[sg.Text("Building Type:",font='Helvitic 12 bold')],[sg.Text("Building Name: ",font='Helvitic 12 bold')],[sg.Text("Owner:",font='Helvitic 12 bold')]]
        colDetails = [[]]

        if(self.building_type == "Normal_Homes" or self.building_type == "Notable_Housing"): # get the title
            colDetails=[[sg.Text("Housing",font='Helvitic 12')],[sg.Text(self.building_name + " of "+ self.owner.name,font='Helvitic 12') ],[sg.Text(self.owner.name,font='Helvitic 12')]]
        else:
            colDetails=[[sg.Text(self.building_type.replace("_"," "),font='Helvitic 12')],[sg.Text(self.building_name,font='Helvitic 12') ],[sg.Text(self.owner.name,font='Helvitic 12')]]
        
        layout = [[sg.Column(colTitle),sg.Column(colDetails)]] # add the title
    
        npc_cols = []
        for value,npc in enumerate(self.occupants):
            npc_cols.append(sg.Column([[sg.Button(npc.name + "\n"+ npc.profession,size=npc_button_size,key=str(value)+"_building")]],vertical_alignment="top"))
        
        layout.append([sg.Frame("Occupants",[npc_cols])])
        if len(self.hooks) != 0:
            layout.append([sg.Text("Hooks",font='Helvitic 12 bold')])
            hooks = []
            for text in self.hooks:
                hooks.append([sg.Text(text)])
            Container = [sg.Column(hooks)]
            layout.append(Container)

        return layout


         