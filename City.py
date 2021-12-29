from ctypes import alignment
from tkinter.constants import FALSE, UNDERLINE
import NPC
import Building
import random as rand
import Generator
import PySimpleGUI as sg
from typing import Container, List


class City():
    city_name = ""
    city_leader = NPC.NPC
    city_pop = 1
    buildings_list:List[Building.Building] = []
    wandering_npcs:List[NPC.NPC] = []
    hooks = []
    LOI = []
    def __init__(self,gen:Generator.generator = None,dict_data = None,multiplier:int = 1):
        self.city_leader = None
        self.city_leader = NPC.NPC(gen)
        if dict_data == None:
            self.city_name = gen.generateCityName()
            self.city_leader = NPC.NPC(gen)
            self.city_leader.profession = "Leader of " + self.city_leader.name
            self.buildings_list = [] #Clear all list to ensure no addons
            self.wandering_npcs = []
            self.hooks = []
            self.LOI = []
            for x in range(0,10*multiplier): # generate buildings
                self.buildings_list.append(Building.Building(gen,Location=self.city_name))
            for x in range(0,10*multiplier-1):
                self.wandering_npcs.append(NPC.NPC(gen))
            for x in range(0,10*multiplier):
                self.LOI.append(gen.generateLOI(natural=rand.randint(0,1),include_city=False))
            
            for x in range(0+multiplier,5*multiplier):
                choice = rand.randint(0,3)
                hook = None
                location = rand.choice(self.LOI)
                match(choice):
                    case 0:
                        hook = gen.generateHook(self.city_leader.name,location=location)
                    case 1:
                        hook = gen.generateHook((rand.choice(self.wandering_npcs)).name,location=location)
                    case 2:
                        hook ="On the nearby Quest Board: " + gen.generateHook(Q_type=1,location=location)
                    case 3:
                        hook =gen.generateHook(Q_type=0,location=location)
                    
                self.hooks.append(hook)
                

    def createDisplay(self):
        layout =[[]]
        colTitle = [[sg.Text("City Name:",font="bold")],[sg.Text("City Population: ",font="bold")],[sg.Text("Local Leader:",font="bold")]]
        colDetails = [[sg.Text(self.city_name)],[sg.Text(self.city_pop)],[sg.Text(self.city_leader.name)]]
        layout=[[sg.Column(colTitle),sg.Column(colDetails)]]
        
        button_size = (24,3) # default button size for buttons
        building_cols = []
        temp_col = [] 
        layout.append([sg.Text("Local Buildings",font="bold")])
        for value, building in enumerate(self.buildings_list):
            if value % 5 == 0 and value != 0:
                building_cols.append(temp_col)
                temp_col = []
            temp_col.append(sg.Button(building.building_name,size=button_size,key=str(value)+"_city"))
        building_cols.append(temp_col)
        Container = [sg.Column(building_cols)]
        layout.append(Container)

        npc_cols = []
        temp_col = []
        temp_col.append(sg.Column(self.city_leader.createDisplay()))
        layout.append([sg.Text("Wandering NPCs",font="bold")])
        for value,npcs in enumerate(self.wandering_npcs):
            if (value+1)% 5 == 0 and value != 0: #starting at +1 to account for the city leader npc
                npc_cols.append(temp_col)
                temp_col = []
            temp_col.append(sg.Column(npcs.createDisplay(),vertical_alignment="top"))
        npc_cols.append(temp_col)
        print(npc_cols)
        Container = [sg.Column(npc_cols)]
        print("Wandering NPCS")
        layout.append(Container)

        layout.append([sg.Text("Nearby Locations of Interest",font="bold")])
        LOI = []
        temp_col = []
        for value,locaiton in enumerate(self.LOI):
            if value % 5 == 0 and value != 0:
                 LOI.append(temp_col)
                 temp_col =[]
            temp_col.append(sg.Text(locaiton))
        LOI.append(temp_col)
        print("\nLOI")
        Container = [sg.Column(LOI)]
        layout.append(Container)

        layout.append([sg.Text("Local Hooks",font="bold")])
        hooks = []
        for hook in self.hooks:
            hooks.append([sg.Text(hook)])
        Container = [sg.Column(hooks)]
        layout.append(Container)

        return layout
        