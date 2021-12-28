from tkinter.constants import FALSE
import NPC
import Building
import random as rand
import Generator
import PySimpleGUI as sg
from typing import List


class City():
    city_name = ""
    city_leader = NPC.NPC
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
            for x in range(0,10*multiplier): # generate buildings
                self.buildings_list.append(Building.Building(gen,Location=self.city_name))
            for x in range(0,10*multiplier):
                self.wandering_npcs.append(NPC.NPC(gen))
            for x in range(0,5*multiplier):
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
                

