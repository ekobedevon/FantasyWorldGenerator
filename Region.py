import NPC
import Building
import City
import random as rand
import Generator
import PySimpleGUI as sg
import Style as s
from typing import List



        

class Region():
    region_name = ""
    political_united = True #if the area has a majority ruled by one group/perosn
    political_system = "TBD" # what system they are under
    political_leader = NPC.NPC # who is leading
    population = 0
    capital = City.City # the main city
    region_powers:List[NPC.NPC] = [] # the major threats to the are
    cities:List[City.City] = [] # the major
    hooks = []
    minor_LOI = []
    major_LOI = []
    

    def __init__(self,gen:Generator.generator = None,multiplier:int = 2,political_united = None):
        self.region_powers:List[NPC.NPC] = [] # make sure all list are clear if regening a variable over and over
        self.cities:List[City.City] = []
        self.hooks = []
        self.minor_LOI = []
        self.major_LOI = []
        named_location_list = []
        system,title,home = gen.generatePoliticalSystem()
        if self.political_united == None:
            self.political_united = rand.randint(0,1) #50/50 if the area is politically united
        if(self.political_united):
            self.capital = City.City(gen) # generate the capital city
            self.region_name = gen.generateRegionName(self.capital.city_name)
            self.political_leader = self.capital.city_leader
            named_location_list.append(self.capital.city_name)
        else:
            self.region_name = gen.generateRegionName("")
            self.capital = None
            self.political_leader = None
            self.political_system = "None"

        for x in range(0,5*(multiplier-1)): #generate region powers
            self.region_powers.append(NPC.NPC(gen))
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
        current_lairs = []
        for power in self.region_powers:
            lair_location = rand.choice(self.minor_LOI)
            while lair_location in current_lairs:
                lair_location = rand.choice(self.minor_LOI)
            power.lair = rand.choice(self.minor_LOI) # set villan lairs
            current_lairs.append(lair_location)
        
        npc_list = [] # used for goal generation
        city_list = [] # used for goal generation
        for city in self.cities:
            city_list.append(city.city_name)
            self.population += city.city_pop # get total popoulation
            for c_npc in city.wandering_npcs:
                npc_list.append(c_npc.name)
            for building in city.buildings_list:
                for b_npc in building.occupants:
                    npc_list.append(b_npc.name)
        
        for power in self.region_powers: # generate powers goals
            power.goals = gen.generatePowerGoal(self.minor_LOI,npc_list,self.major_LOI,"Current Region",self.political_leader.name,city_list)

        if self.capital == None: # even out cities
            self.cities.append(City.City(gen))
        else: # set political system information
            self.political_system = system
            if system == "Theocratic Authoritarian":
                temp = home.partition("Diety")
                temp_domain = temp[1]+temp[2]
                temp_domain = temp_domain.removesuffix(" domain") #remove the domain
                temp_domain = temp_domain.replace("the ","",1) # remove "the"
                self.political_leader.profession = title + ",Follower of the " +temp_domain
            else:
                self.political_leader.profession = title
            if home != "":
                leader_building  = Building.Building(gen)
                leader_building.building_name = home
                leader_building.owner = self.political_leader
                leader_building.hooks = []
                leader_building.occupants[0] = self.political_leader
                npc_list = []
                for npc in leader_building.occupants:
                    npc_list.append(npc.name)
                for x in range(0,3):
                    leader_building.hooks.append(gen.generateHook(rand.choice(npc_list),location_list=self.major_LOI + self.minor_LOI))
                self.capital.buildings_list[0] = leader_building
            self.cities.insert(0,self.capital)


    def createDisplay(self):
        button_size = (30,3)
        layout =[[]]
        colTitle = [[sg.Text("Region Name:",font=s.Title_Style)],[sg.Text("Region Pop:",font=s.Title_Style)],[sg.Text("Political System:",font=s.Title_Style)]]
        colDetails = [[sg.Text(self.region_name,font=s.Title_Size_Style)],[sg.Text(self.population,font=s.Title_Size_Style)],[sg.Text(self.political_system,font=s.Title_Size_Style)]]
        if self.political_leader != None:
            colTitle.append([sg.Text("Region Leader:",font=s.Title_Style)])
            colDetails.append([sg.Text(self.political_leader.name + " in " + self.capital.city_name,font=s.Title_Size_Style)])
        layout=[[sg.Column(colTitle),sg.Column(colDetails)]]

        city_cols = []
        temp_col = []
        for value,city in enumerate(self.cities):
            if value % 5 == 0 and value != 0:
                city_cols.append(temp_col)
                temp_col = []
            temp_col.append(sg.Button(city.city_name,size=button_size,key=str(value)+"_city_region"))
        city_cols.append(temp_col)
        Container = [sg.Frame("Cities",city_cols)]
        layout.append(Container)

        npc_cols = []
        temp_col = []
        for value,npc in enumerate(self.region_powers):
            if (value)% 5 == 0 and value != 0: #starting at +1 to account for the city leader npc
                npc_cols.append(temp_col)
                temp_col = []
            temp_col.append(sg.Button(npc.name.capitalize(),size=button_size,key=str(value) + "_npc_region"))
        npc_cols.append(temp_col)
        Container = [sg.Frame("Regional Powers",layout=npc_cols)]
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


        layout.append([sg.Text("Regional Hooks",font=s.Title_Style)])
        hooks = []
        for hook in self.hooks:
            hooks.append([sg.Text(hook)])
        Container = [sg.Column(hooks)]
        layout.append(Container)





        return layout
                
            

        




        