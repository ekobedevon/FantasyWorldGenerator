from random import choice, randint
from tkinter import font
from tkinter.font import BOLD
from typing import Container
import NPC
import Generator
import PySimpleGUI as sg 


class Building():
    building_type = ""
    building_name = ""
    owner = None
    occupants = []
    hooks = []
    def __init__(self,gen: Generator.generator = None,dict_data = None):
        self.owner =None
        self.owner = NPC.NPC(gen=gen)
        if dict_data == None:
            building_name, building_owner, building_type = gen.generateBuilding()
            self.building_type = building_type
            self.building_name = building_name
            if building_owner != "": #if the building is not a house
                self.owner.profession = building_owner
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
    
    def createDisplay(self):
        layout = [[]]
        colTitle = [[sg.Text("Building Type:",font="bold")],[sg.Text("Building Name: ",font="bold")],[sg.Text("Owner:",font="bold")]]
        colDetails = [[]]

        if(self.building_type == "Normal_Homes" or self.building_type == "Notable_Housing"): # get the title
            colDetails=[[sg.Text("Housing")],[sg.Text(self.building_name + " of "+ self.owner.name) ],[sg.Text(self.owner.name)]]
        else:
            colDetails=[[sg.Text(self.building_type.replace("_"," "))],[sg.Text(self.building_name) ],[sg.Text(self.owner.name)]]
        
        layout = [[sg.Column(colTitle),sg.Column(colDetails)]] # add the title
    

        npc_cols = []
        npc_cols.append(sg.Column(self.owner.createDisplay()))

        for npcs in self.occupants:
            npc_cols.append(sg.Column(npcs.createDisplay(),vertical_alignment="top"))
        
        
        layout.append(npc_cols)
        if len(self.hooks) != 0:
            layout.append([sg.Text("Hooks",font="bold")])
            hooks = []
            for text in self.hooks:
                hooks.append([sg.Text(text)])
            Container = [sg.Column(hooks)]
            layout.append(Container)
            
            """layout.append(hooks)"""

        return layout


         