import NPC
import Building
import City
import Region
import random as rand
import Generator
import PySimpleGUI as sg
import Style as s
from typing import List

class Continent():
    continent_name = ""
    political_united = True #if the area has a majority ruled by one group/perosn
    political_system = "TBD" # what system they are under
    political_leader = NPC.NPC # who is leading
    population = 0
    capital = City.City # the main city
    continent_powers:List[NPC.NPC] = [] # the major threats to the are
    regions:List[Region.Region] = [] # the major
    minor_LOI = []
    major_LOI = []

    def __init__(self,gen:Generator.generator = None,multiplier:int = 2,political_united = None):
        self.region_powers:List[NPC.NPC] = [] # make sure all list are clear if regening a variable over and over
        self.regions:List[Region.Region] = []
        self.hooks = []
        self.minor_LOI = []
        self.major_LOI = []
        #variables only used in generation
        main_region = None
        current_lairs = []
        npc_list = []
        locations = []

        if self.political_united == None:
            self.political_united = rand.randint(0,1) #50/50 if the area is politically united
        if(self.political_united):
            main_region = Region.Region(gen,political_united=True) # generate a region
            self.capital = main_region.capital # set the capital of the continent from the main region
            self.political_system = main_region.political_system
           # self.region_name = gen.generateRegionName(self.capital.city_name)
            self.political_leader = main_region.political_leader # set the continent political leader from the main region
            self.continent_name = main_region.region_name
            main_region.region_name = gen.generateRegionName()
        else:
            main_region = Region.Region(gen) # generate a region to use to even out the above 
            self.region_name = gen.generateRegionName("")
            self.capital = None
            self.political_leader = None
            self.political_system = "None"

        self.regions.append(main_region) #add the first region to the list

        for x in range(0,5*(multiplier-1)): #generate region powers
            self.continent_powers.append(NPC.NPC(gen))
        for x in range(0,5*multiplier-1):#generate cities to populate region
            self.regions.append(Region.Region(gen))
        for x in range(0,5*multiplier-1): #generate minor locations of interst
            self.minor_LOI.append(gen.generateLOI(include_city=False))
        for x in range(0,2*multiplier): # generate major locations of interest
            self.major_LOI.append(gen.generateLOI(include_city=False))
        for r in self.regions: # append cities to named location list
            for c in r.cities:
                locations.append(c.city_name) # add all cities to city list
            locations.append(r.region_name)
            npc_list.append(r.capital.city_leader.name) # add all city leaders to the npc list
             
     # all named locations
        for power in self.continent_powers: # for all powers, give them a lair
            lair_location = rand.choice(self.minor_LOI)
            while lair_location in current_lairs: # while the current lair is not unique
                lair_location = rand.choice(self.minor_LOI)
            power.lair = rand.choice(self.minor_LOI) # set villan lairs
            current_lairs.append(lair_location) #added location list

        for power in self.continent_powers: # generate powers goals
            gen.generatePowerGoal(minor_locations=self.minor_LOI,npcs=npc_list,major_locations=self.major_LOI,area_name="CONTINENT",local_leader=self.political_leader.name,cities=locations)

        
            


        
        

        