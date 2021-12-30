from tkinter.constants import TRUE
import NPC
import Building
import City
import random as rand
import Generator
import PySimpleGUI as sg
import Style as s
from typing import List


class regional_power(NPC.NPC):
    lair = ""

    def __init__(self, gen: Generator.generator = None, dict_data=None, isAdult: bool = True, goals: str = ""):
        super().__init__(gen=gen, dict_data=dict_data, isAdult=isAdult, goals=goals)
        self.lair = ""
        

class Region():
    political_united = True #if the area has a majority ruled by one group/perosn
    political_system = "" # what system they are under
    political_leader = NPC.NPC # who is leading
    capital = City.City # the main city
    region_powers:List[regional_power] = [] # the major threats to the are
    cities:List[City.City] = [] # the major
    hooks = []
    minor_LOI = []
    major_LOI = []
    

    def __init__(self,gen:Generator.generator = None,multiplier:int = 2,political_united = None):
        self.region_powers:List[regional_power] = [] # make sure all list are clear if regening a variable over and over
        self.cities:List[City.City] = []
        self.hooks = []
        self.minor_LOI = []
        self.major_LOI = []
        self.RP_lairs = {}
        named_location_list = []
        if self.political_united == None:
            self.political_united = rand.randint(0,1) #50/50 if the area is politically united
        if(self.political_united):
            self.capital = City.City(gen) # generate the capital city
            self.political_leader = self.capital.city_leader
            named_location_list.append(self.capital.city_name)
        else:
            self.capital = None
            self.political_leader = None
            self.political_system = None

        for x in range(0,2*multiplier): #generate region powers
            self.region_powers.append(regional_power(gen))
        for x in range(0,5*multiplier-1):#generate cities to populate region
            self.cities.append(City.City(gen))
        for x in range(0,5*multiplier-1): #generate minor locations of interst
            self.minor_LOI.append(gen.generateLOI(include_city=False))
        for x in range(0,2*multiplier): # generate major locations of interest
            self.major_LOI.append(gen.generateLOI(include_city=False))
        for c in self.cities: # append cities to named location list
            named_location_list.append(c.city_name)
        named_location_list += self.major_LOI + self.minor_LOI
        for x in range(0,5*multiplier):
            self.hooks.append(gen.generateHook(location_list=named_location_list))
        for power in self.region_powers:
            lair_location = rand.choice(self.minor_LOI)
            while lair_location in self.RP_lairs.values():
                lair_location = rand.choice(self.minor_LOI)
            power.lair = rand.choice(self.minor_LOI) # set villan lair

        




        