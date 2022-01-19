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
    capital = City.City # the main city
    continent_powers:List[NPC.NPC] = [] # the major threats to the are
    regions:List[Region.Region] = [] # the major
    minor_LOI = []
    major_LOI = []
    sumPop = 0
    def __init__(self,gen:Generator.generator = None,multiplier:int = 2,political_united = None):
        self.continent_powers:List[NPC.NPC] = [] # make sure all list are clear if regening a variable over and over
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
            self.continent_name = gen.generateWorldName()
            
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
        for x in range(0,10*multiplier-1): #generate minor locations of interst
            self.minor_LOI.append(gen.generateLOI(include_city=False))
        for x in range(0,2*multiplier): # generate major locations of interest
            self.major_LOI.append(gen.generateLOI(include_city=False))
        for r in self.regions: # append cities to named location list
            for c in r.cities:
                locations.append(c.city_name) # add all cities to city list
            locations.append(r.region_name)
            npc_list.append(r.capital.city_leader.name) # add all city leaders to the npc list
            self.sumPop += r.population

     # all named locations
        for power in self.continent_powers: # for all powers, give them a lair
            lair_location = rand.choice(self.minor_LOI)
            while lair_location in current_lairs: # while the current lair is not unique
                lair_location = rand.choice(self.minor_LOI)
            power.lair = rand.choice(self.minor_LOI) # set villan lairs

        for power in self.continent_powers: # generate powers goals
            power.goals = gen.generatePowerGoal(minor_locations=self.minor_LOI,npcs=npc_list,major_locations=self.major_LOI,area_name="CONTINENT",local_leader=self.political_leader.name,cities=locations)

    
        
            
    def createDisplay(self):
        button_size = (30,3)
        layout =[[]]
        colTitle = [[sg.Text("Continent Name:",font=s.Title_Style)],[sg.Text("Continent Pop:",font=s.Title_Style)],[sg.Text("Political System:",font=s.Title_Style)]]
        colDetails = [[sg.Text(self.continent_name,font=s.Title_Size_Style)],[sg.Text(self.sumPop,font=s.Title_Size_Style)],[sg.Text(self.political_system,font=s.Title_Size_Style)]]
        if self.political_leader != None:
            colTitle.append([sg.Text("Region Leader:",font=s.Title_Style)])
            colDetails.append([sg.Text(self.political_leader.name + " in " + self.capital.city_name,font=s.Title_Size_Style)])
        layout=[[sg.Column(colTitle),sg.Column(colDetails)]]

        region_col = []
        temp_col = []

        for value,region in enumerate(self.regions):
            if value % 5 == 0 and value !=0:
                region_col.append(temp_col)
                temp_col = []
            temp_col.append(sg.Button(region.region_name,size=button_size,key=str(value)+"_region_cont"))
        region_col.append(temp_col)
        Container = [sg.Frame("Regions",region_col)]
        layout.append(Container)

        npc_cols = []
        temp_col = []
        for value,npc in enumerate(self.continent_powers):
            if (value)% 5 == 0 and value != 0: #starting at +1 to account for the city leader npc
                npc_cols.append(temp_col)
                temp_col = []
            temp_col.append(sg.Button(npc.name.capitalize(),size=button_size,key=str(value) + "_npc_cont"))
        npc_cols.append(temp_col)
        Container = [sg.Frame("Continental Powers",layout=npc_cols)]
        layout.append(Container)

        layout.append([sg.Text("Major Locations of Interest",font=s.Title_Style)])
        LOI = []
        temp_col = []
        for value,locaiton in enumerate(self.major_LOI):
            if value % 5 == 0 and value != 0:
                 LOI.append(temp_col)
                 temp_col =[]
            temp_col.append(sg.Text(locaiton))
        LOI.append(temp_col)
        Container = [sg.Column(LOI)]
        layout.append(Container)

        layout.append([sg.Text("Minor Locations of Interest",font=s.Title_Style)])
        LOI = []
        temp_col = []
        for value,locaiton in enumerate(self.minor_LOI):
            if value % 5 == 0 and value != 0:
                 LOI.append(temp_col)
                 temp_col =[]
            temp_col.append(sg.Text(locaiton))
        LOI.append(temp_col)
        Container = [sg.Column(LOI)]
        layout.append(Container)

        return layout
        
        

        