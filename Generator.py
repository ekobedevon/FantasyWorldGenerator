import json as js
import os
import random as rand
import math
from typing import List


def initialize_race(race: str):
    """Used to get all the information for each race in the Json File folder for races"""
    path = "./" + race + "/" #set the path for this folder
    file_list = os.listdir(path) #get all file names in the folder
    race_dict = {}
    if "Settings.json" not in file_list: #if settings not present,then race is not valid
        return -1
    for file_name in file_list: #store all the json files in a dict
            file = open(path + file_name);
            race_dict[file_name.removesuffix('.json')] = js.load(file)
    if len(race_dict["Settings"]) < 3 : #if settings doesn't have current minimum settings
        return -1
    return race_dict

def intialize_professions():
    """Read in from the professions files and generate the lists needed for world generation"""
    os.chdir("Json_Files\Professions") #set to profession directory
    profession_fileList = os.listdir("./")
    profession_master=[] #list of ALL professions
    professions_Categorized = {} #professions sorted by categories
    for file_name in profession_fileList:
        file = open(file_name);
        data = js.load(file) # load the data into an list
        profession_master = profession_master + data # add the list to the master
        professions_Categorized[file_name.removesuffix(".json")] = data #store in dicitonary
    return profession_master,professions_Categorized

def intialize_building_names():
    """Read in files from the buildings folder and store then in the proper lists needed for world generation"""
    os.chdir("Json_Files\Buildings\Building_Details") # set to building directory
    building_fileList = os.listdir("./")
    building_name_details = {}
    for file_name in building_fileList:
        file = open(file_name)
        data = js.load(file)
        building_name_details[file_name.removesuffix(".json")] = data
    return building_name_details

def intialize_building_types():
    os.chdir("Json_Files\Buildings")
    file = open("Building_Types.json")
    data = js.load(file)
    building_types = data
    building_types_names  = {}
    os.chdir("./Building_Types_Names")
    building_fileList = os.listdir("./")
    for file_name in building_fileList:
        file = open(file_name)
        data = js.load(file)
        building_types_names[file_name.removesuffix(".json")] = data
    
    return building_types, building_types_names


def initlalize_general_details():
    """Read in files from the General details folder and store then in the proper lists needed for world generation"""
    os.chdir("Json_Files\General_Details")
    general_fileList = os.listdir("./")
    general_details  = {}
    for file_name in general_fileList:
        file = open(file_name)
        data = js.load(file)
        general_details[file_name.removesuffix(".json")] = data
    return general_details

def intialize_item_details():
    """Read in files from item folder and store them in a dictionary"""
    os.chdir("Json_Files\Items")
    general_fileList = os.listdir("./")
    item_details = {}
    for file_name in general_fileList:
        file = open(file_name)
        data = js.load(file)
        item_details[file_name.removesuffix(".json")] = data
    return item_details

def intialize_quest_details():
    os.chdir("Json_Files\Quest_Details")
    general_fileList = os.listdir("./")
    quest_details = {}
    for file_name in general_fileList:
        file = open(file_name)
        data = js.load(file)
        quest_details[file_name.removesuffix(".json")] = data
    return quest_details

def intialize_location_details():
    os.chdir("Json_Files\Location")
    general_fileList = os.listdir("./")
    location_details = {}
    for file_name in general_fileList:
        file = open(file_name)
        data = js.load(file)
        location_details[file_name.removesuffix(".json")] = data
    return location_details

def intialize_city_details():
    os.chdir("Json_Files\Cities")
    general_fileList = os.listdir("./")
    city_details = {}
    for file_name in general_fileList:
        file = open(file_name)
        data = js.load(file)
        city_details[file_name.removesuffix(".json")] = data
    return city_details

def intialize_origins():
    os.chdir("Json_Files\Origins") # enter origin folder
    origin_list  = os.listdir("./") # get all list of origins
    base = os.getcwd() # get base directory
    origin_details = {} # create dictionary
    for folder in origin_list:
        os.chdir("./"+folder) # got into the folder of each origin
        details = os.listdir("./") #get all directories in this folders
        if len(details) == 4: # if there are not exactly 4 files
            origin_details[folder] = {} # create a sub dictionary
            for file_name in details: # for each file in the specific folder
                file = open(file_name) 
                data = js.load(file)
                origin_details[folder][file_name.removesuffix(".json")] = data
        else:
            print("Invalid Parameters")
        os.chdir(base)

    return origin_details
        
        

def generateGender():
    """50/50 chance to generate either gender"""
    if (rand.randint(0,1)) == 0:
        return "M"
    else:
        return "F"

class generator(): # create a generator object
    #Class Variables
    race_list = {} # a dictionary of all the races
    profession_master=[] #master list of all jobs
    professions_Categorized = {} #jobs sorted by categories
    building_names = {} #building name details
    building_types = []
    building_types_names  = {}
    general_details = {} #details that might be used between multiple generators
    item_details = {} #details used for item generation
    location_details = {}
    quest_details = {}
    city_details = {}
    origin_details = {}
    pantheon = {} #list to hold all gods
    #create a generator object that stores all the data at the start
    def __init__(self):
        base = os.getcwd()
        os.chdir("Json_Files\Races")
        race_fileList = os.listdir("./") # all races in the files
        for race in race_fileList:
            data = initialize_race(race) 
            if type(data) != type(1): #if the data type is not an int
                self.race_list[race] = data # store in data
            else:
                print(race + " is not in a valid format, checking settings file in race folder")
        os.chdir(base)
        self.profession_master, self.professions_Categorized = intialize_professions() #intialize profession master
        os.chdir(base)
        self.building_names = intialize_building_names()
        os.chdir(base)
        self.general_details = initlalize_general_details()
        os.chdir(base)
        self.building_types, self.building_types_names = intialize_building_types()
        os.chdir(base)
        self.item_details = intialize_item_details()
        os.chdir(base)
        self.location_details = intialize_location_details()
        os.chdir(base)
        self.quest_details = intialize_quest_details()
        os.chdir(base)
        self.city_details = intialize_city_details()
        os.chdir(base)
        self.origin_details = intialize_origins()
        os.chdir(base)

        for domain in self.general_details["Domains"]:
            self.pantheon[domain] = self.generateGodName(domain=domain)



    def generateRace(self):
        if len(self.race_list) != None:
            list_keys = list(self.race_list.keys())
            return rand.choice(list_keys)


    def generateName(self,race: str, sex: str):
        """Generate a name base on parameters

        Args:
            race (str, optional): The race of the person that needs the name. Defaults to "".
            sex (str, optional): The sex of the person that needs the name. Defaults to "".

        Returns:
            [str]: returns a name
        """
        name_convention = self.race_list[race]["Settings"]["Name Convention"]
        name = ""
        match (name_convention):
            case 0:
                print("Not enough arguments")
            case 1:
                name = rand.choice(self.race_list[race]["Genderless"])
            case 2:# races with last names from other races
                if sex == "M" or sex == "F":
                    name = rand.choice(self.race_list[race][race+"_"+sex])
                keys = self.race_list[race]["Settings"]
                if "Origins" not in list(keys.keys()): # if no orgins key is present
                    print("Settings file not correct, race has no origins for last name, returning first name only")
                else: 
                    origin = self.race_list[race]["Settings"]["Origins"] # get origin list
                    race = rand.choice(origin) #get a race from the origin list
                    last_name_patern = self.race_list[race]["Settings"]["Name Convention"] # get the last name pattern of the parent race
                    match(last_name_patern): #
                        case 3: # standard last name pattern
                            name = name + " " + rand.choice(self.race_list[race][race+"_Last"])
                        case 4: # complex last name
                            name = name + " of " + rand.choice(self.race_list[race][race+"_Pre"])  + " " + rand.choice(self.race_list[race][race+"_Post"])
            case 3: #races with simple last names
                if sex == "M" or sex == "F":
                    name = rand.choice(self.race_list[race][race+"_"+sex])
                name = name + " " + rand.choice(self.race_list[race][race+"_Last"])
            case 4: #races with complex last names(2 parts)
                if sex == "M" or sex == "F":
                    name = rand.choice(self.race_list[race][race+"_"+sex])
                name = name + " of " + rand.choice(self.race_list[race][race+"_Pre"])  + " " + rand.choice(self.race_list[race][race+"_Post"])
        return name

    def generateGodName(self,race:str = "",sex: str= "",domain:str = ""): # seperate method in order to allow easier change down the line
        """Generate a god name base on parameters

        Args:
            race (str, optional): The race of the person that needs the name. Defaults to "".
            sex (str, optional): The sex of the person that needs the name. Defaults to "".
            domain (str, optional): The desired domain of the god. Defaults to "".

        Returns:
            [type]: [description]
        """
        if race == "":
            race =self.generateRace()
        if sex == "":
            sex = generateGender()
        if domain == "":
            domain = rand.choice(self.general_details["Domains"])
        return self.generateName(race,sex) +", Diety of the "+ domain + " domain"

    def generateProfession(self,category: str = ""):
        job = ""
        if category == "":
            job = rand.choice(self.profession_master)
        elif category in self.professions_Categorized:
            job = rand.choice(self.professions_Categorized[category])
        else:
            print("Invalid category, returning random profession")
            job = rand.choice(self.profession_master)
        return job
        
    def generateAge(self,race: str = "Human",isAdult: bool = True):
        """Given proper parameter, returns an appororaite age for a given race

        Args:
            race (str, optional): The race of the person. Defaults to "Human".
            isAdult (bool, optional): If the npc is a adult. Defaults to True.

        Returns:
            [int]: the age
        """
        max_age = self.race_list[race]["Settings"]["Max_Age"]
        maturity = self.race_list[race]["Settings"]["Maturity"]
        multiplier = rand.uniform(0,1)
        if isAdult:
            age = maturity + (max_age * multiplier ** 2)
            return math.floor(age)
        else:
            age = maturity - (maturity* multiplier ** 2)
            return math.floor
        
    def generateTavernName(self):
        """Generates a random taven name

        Returns:
            [str]: tavern name
        """
        name = ""
        num = rand.randint(0,9)
        match(num):
            case 0:
                name = rand.choice(self.building_names["Adjectives"]) + " " + rand.choice(self.building_names["Nouns"])
            case 1:
                name = rand.choice(self.building_names["Adjectives"]) + " " + rand.choice(self.building_names["Nouns"]) + " " + rand.choice(self.building_names["Bar_Titles"])
            case 2:
                name = "The " + rand.choice(self.building_names["Adjectives"]) + " " + rand.choice(self.building_names["Nouns"])
            case 3:
                name = "The " + rand.choice(self.building_names["Adjectives"]) + " " + rand.choice(self.building_names["Nouns"]) + " " + rand.choice(self.building_names["Bar_Titles"])
            case 4:
                name = rand.choice(self.building_names["Nouns"]) + " & " + rand.choice(self.building_names["Nouns"])
            case 5:
                name = rand.choice(self.building_names["Nouns"]) + " & " + rand.choice(self.building_names["Nouns"]) + " " + rand.choice(self.building_names["Bar_Titles"])
            case 6:
                name = "The " + rand.choice(self.building_names["Nouns"]) + " & " + rand.choice(self.building_names["Nouns"])
            case 7:
                name = "The " + rand.choice(self.building_names["Nouns"]) + " & " + rand.choice(self.building_names["Nouns"]) + " " + rand.choice(self.building_names["Bar_Titles"])
            case 8:
                name = rand.choice(self.building_names["Adjectives"]) + " " + rand.choice(self.building_names["Bar_Titles"])
            case 9:
                name = "The " + rand.choice(self.building_names["Adjectives"]) + " " + rand.choice(self.building_names["Bar_Titles"])

        return name

    def generateBuildingName(self):
        """Generates a random building name

        Returns:
            [str]: building name
        """
        name = ""
        num = rand.randint(0,3)
        match(num):
            case 0:
                name = rand.choice(self.building_names["Adjectives"]) + " " + rand.choice(self.building_names["Nouns"])
            case 1:
                name = "The " + rand.choice(self.building_names["Adjectives"]) + " " + rand.choice(self.building_names["Nouns"])
            case 2:
                name = rand.choice(self.building_names["Nouns"]) + " & " + rand.choice(self.building_names["Nouns"])
            case 3:
                name = "The " + rand.choice(self.building_names["Nouns"]) + " & " + rand.choice(self.building_names["Nouns"])
        return name

    def generateReligiousBuildingName(self,diety:str = ""):
        """Generates a random taven name
        Args:
            domain (str, optional): The desired god for the building . Defaults to a randomly generater diety.

        Returns:
            [str]: Religious Building name
        """
        if diety == "":
            diety =rand.choice(list(self.pantheon.values()))
        name = rand.choice(self.building_names["Worship_Titles"]) + " of " + diety
        return name

    def generateBuilding(self,building_type: str = "",location: str = ""):
        """ Generates the details needed for a building based 

        Args:
            building_type (str, optional): The type of building to be generated. Defaults to "".
                Vailid Building Types: Shops,Tavern,Guild_Types,Normal_Homes,Notable_Housing,Government Buidling,Craftsmen,Religious
            location (str, optional): The city in which the building is located, if desired. Defaults to "".

        Returns:
            [str]: name of builidng
            [str]: profession of owner
            [str]: type of builidng
        """
        building_name = ""
        owner_proffesion = ""
        suffix = ""
        if location != "":
            suffix = " of " + location 
        if building_type == "" or building_type not in self.building_types: #if their is no building type or if the building type is not valid
            building_type = rand.choice(self.building_types) # generate a building type
        match(building_type):
            case "Shops":
                building_name = self.generateBuildingName()
                owner_proffesion = "Owner of " + building_name
            case "Tavern":
                building_name = self.generateTavernName()
                owner_proffesion = "Owner of " + building_name
            case "Guild_Types":
                building_name = rand.choice(self.building_types_names["Guild_Types"]) + " Guild Branch" + suffix
                owner_proffesion = "Leader of local " + building_name
            case "Normal_Homes":
                building_name = rand.choice(self.building_types_names["Normal_Homes"])
                owner_proffesion = ""
            case "Government Building":
                building_name = "Government Building" + suffix
                owner_proffesion = "Leader for local government"
            case "Notable_Housing":
                building_name = rand.choice(self.building_types_names["Notable_Housing"])
                owner_proffesion = ""
            case "Craftsmen":
                building_name = self.generateBuildingName() + " " + rand.choice(self.building_types_names['Craftsmen'])
                owner_proffesion = "Owner of " + building_name
            case "Religious":
                building_name = self.generateReligiousBuildingName()
                diety_name = building_name.partition(" of ")
                owner_proffesion = " of " + diety_name[2]

        return building_name, owner_proffesion,building_type
            
    def generateMacguffin(self,item_type: str = None):
        """[summary]

        Args:
            item_type (str, optional): the type of item desired. Defaults to None.

        Returns:
            [str]: item name
        """
        name =""
        if item_type == None or item_type not in self.item_details["Item_Types"]:# generate a item type if no valid item is given
            item_base  = rand.choice(self.item_details["Item_Types"])

        if item_base == "Armor" or item_base == "Weapon": # if it is armor or weapon type
            name = rand.choice(self.item_details[item_base]) #chose from armor/weapon list
        else:
            name = item_base #asign item type to name

        if(rand.randint(0,2) == 0): # pick either of two name formates, weighted for non named items
            name = name + " of " + self.generateName(self.generateRace(),generateGender()) 
        else:
            name = name + " of " + rand.choice(self.item_details["Item_Preffix"]) + " " + rand.choice(self.item_details["Item_Suffix"])
        return name # return name

    def generateHook(self,quest_giver: str = None,target: str = None,location: str = None,location_list = [] ,reward: str = None,Q_type: int = 1):
        hook = None
        if quest_giver == None: #generate quest giver name if not given one
            quest_giver = self.generateName(self.generateRace(),generateGender())

        if reward == None:
            if(rand.randint(0,1)):
                reward = "level appropriate gold amount"
            else:
                reward = self.generateMacguffin() + " and level appropriate gold amount"
        if location == None:
            location = self.generateLOI()
        if len(location_list) != 0: #if given a list of locations, generate from that list
            location = rand.choice(location_list)
        
        if rand.randint(0,1) and Q_type == 1:
            party_verb = rand.choice(self.quest_details["Kill_Synonyms"])
            if target == None: # if no target given, generate a monster to target
                target = rand.choice(self.general_details["Monsters"]) + "(s)"
            objective_verb = rand.choice(self.quest_details["Oppresive_synonyms"])
            hook = quest_giver + " wants to hire the party to " + party_verb + " the " + target + " that have been " + objective_verb + " the " + location + " and will pay them with a " + reward + "."
        else:
            party_verb = rand.choice(self.quest_details["Find_Synonyms"])
            guide_item = rand.choice(self.quest_details["Map_Alternates"])
            
            hook = "The Party " + party_verb + " a " + guide_item + " that leads them to the " + location + ", the " + guide_item + " leads them to believe there is a " + reward + " located somewhere inside."
        return hook
            
    def generateLOI(self,natural: bool = None,include_city: bool = True):
        """Generate a Location of interest"""
        if natural == None:
            natural = rand.randint(0,1)
        location_type = ""
        if natural:
            location_type = rand.choice(self.location_details["Locations_Natural"])
        else:
            location_type = rand.choice(self.location_details["Locations_ManMade"])
        name = ""
        match(rand.randint(0,5)):
            case 0:
                name = location_type + " of " + rand.choice(self.location_details["Adjectives"]) + " " + rand.choice(self.location_details["Noun"])
            case 1:
                name = location_type + " of " + rand.choice(self.location_details["Noun"])
            case 2:
                name = "The " + rand.choice(self.location_details["Adjectives"]) + " " + location_type
            case 3:
                name = rand.choice(self.location_details["Adjectives"]) + " " + location_type
            case 4:
                name = rand.choice(self.location_details["Adjectives"]) + " " + rand.choice(self.location_details["Noun"]) + " " + location_type
            case 5:
                if(include_city):
                    name = "city of " + self.generateCityName()
                else:
                    match(rand.randint(0,3)):
                        case 0:
                            name = location_type + " of " + rand.choice(self.location_details["Adjectives"]) + " " + rand.choice(self.location_details["Noun"])
                        case 1:
                            name = location_type + " of " + rand.choice(self.location_details["Noun"])
                        case 2:
                            name = "The " + rand.choice(self.location_details["Adjectives"]) + " " + location_type
                        case 3:
                            name = rand.choice(self.location_details["Adjectives"]) + " " + location_type
                    

        return name

    def generateInterstingName(self,owner: str,b_type:str):
        name = ""
        match(rand.randint(0,5)):
            case 0:
                name = b_type + " of " + rand.choice(self.location_details["Adjectives"]) + " " + rand.choice(self.location_details["Noun"])
            case 1:
                name = b_type + " of " + rand.choice(self.location_details["Noun"])
            case 2:
                name = "The " + rand.choice(self.location_details["Adjectives"]) + " " + b_type
            case 3:
                name = rand.choice(self.location_details["Adjectives"]) + " " + b_type
            case 4:
                name = rand.choice(self.location_details["Adjectives"]) + " " + rand.choice(self.location_details["Noun"]) + " " + b_type
            case 5:
                name = b_type+ " of " + owner
        return name

    def generateCityName(self):
        return rand.choice(self.city_details["Name_Start"]) + rand.choice(self.city_details["Name_Endings"]).lower()

    def generateWorldName(self):
        return rand.choice(self.location_details["World Titles"]) + " of " + rand.choice(self.location_details["Adjectives"]) +  " " + rand.choice(self.location_details["Noun"])


    def generateOrigin(self,origin: str = ""):
        if origin == "":
            origins = list(self.origin_details.keys())
            origin = rand.choice(origins)
        origin_Details = {}
        for detail in self.origin_details[origin]:
            origin_Details[detail] = rand.choice(self.origin_details[origin][detail])
        return origin,origin_Details
    
    def generateRegionName(self,region_name: str = ""):
        location_type = rand.choice(self.location_details["Locations_Natural"])
        if region_name != "":
            return location_type + " " + region_name
        else:
            match(rand.randint(1,4)):
                case 1:
                    return location_type + " of " + rand.choice(self.location_details["Adjectives"]) +  " " + rand.choice(self.location_details["Noun"])
                case 2:
                    return rand.choice(self.location_details["World Titles"]) + " of " + rand.choice(self.location_details["Adjectives"]) +  " " + rand.choice(self.location_details["Noun"])
                case 3:
                    return "The " + rand.choice(self.location_details["Adjectives"]) + " " + location_type
                case 4: 
                    return "The " + rand.choice(self.location_details["Adjectives"]) + " " + rand.choice(self.location_details["Noun"]) + " " + location_type


    def generatePowerGoal(self,minor_locations ,npcs ,major_locations,area_name,local_leader,cities):
        """Generates a Goal for a npc based on paramerters given

        Args:
            minor_locations (list[str]): a list of locations
            npcs (list[str]): a list of npc names
            major_locations (list[str]): a list of locations
            area_name (list[str]): name of the overall location
            local_leader (list[str]): name of local leader
            cities (list[str]): a list of city names

        Returns:
            [str]: A 1 line goal with motive and means of achieving
        """
        if local_leader == "":
            local_leader = self.generateName(self.generateRace(),generateGender())
        Goal = ""
        Avaiable_actions = []
        match(rand.randint(1,6)):
            case 1: #REVENGE
                match(rand.randint(1,4)): #type of revenge
                    case 1:
                        Goal = "Revenge on " + (rand.choice(npcs)) #revenge on a person
                    case 2:
                        Goal = "Revenge on " + (rand.choice(npcs)) + "'s ancestors" #revenge on a blood line
                    case 3:
                        Goal = "Revenge on all" + (rand.choice(list(self.race_list.keys()))) #Revenge on a race
                    case 4:
                        Goal = "Revenge on all inhabitants of " + (rand.choice(major_locations))
            case 2: #DOMINATION
                match(rand.randint(1,3)):
                    case 1:
                        Goal = "Rule over " + rand.choice(minor_locations) # rule over a non city place
                    case 2:
                        Goal = "Rule over " + rand.choice(cities) # rule over a city
                    case 3:
                        Goal = "Complete Rule over " + area_name
            case 3: # ACQUISITON Of X
                match(rand.randint(1,6)):
                    case 1:
                        Goal = "To acquire " + self.generateMacguffin() #to get an item
                    case 2:
                        Goal = "To get " + self.generateMacguffin() + " back from " + rand.choice(npcs) # to get an item back from someone
                    case 3:
                        Goal = "To get " + self.generateMacguffin() + " back from " + rand.choice(minor_locations + major_locations) # to get an item back from somewhere
                    case 4:
                        Goal = "To get/steal the affection of " + rand.choice(npcs) # to steal someones love
                    case 5:
                        Goal = "To steal the title of " + rand.choice(npcs) # to steal the title from someone
                    case 6:
                        Goal = "To steal the birthwright of " + rand.choice(npcs) # to steal someone's birthwrite
            case 4: #Life or death
                match(rand.randint(1,4)):
                    case 1: 
                        Goal = "To achieve Lichdom"
                    case 2:
                        Goal = "To achieve Immortality"
                    case 3:
                        Goal = "To escape Immortality and truly die"
                    case 4:
                        Goal = "To resurect someone their true love"
            case 5: # A power beyond
                match(rand.randint(1,4)):
                    case 1:
                        Goal = "To ascend to godhood"
                    case 2:
                        Goal = "To kill a god"
                    case 3:
                        Goal = "To summon a god"
                    case 4:
                        Goal = "To open a portal to another plane/world"
            case 6: #to amass power
                match(rand.randint(1,2)):
                    case 1:
                        Goal = "To become insanely wealthy"
                    case 2:
                        Goal = "To become insanely powerful"
                
        means_of_action = ""

        match(1): 
            case 1: # TO STEAL SOMETHING
                match(rand.randint(1,2)):
                    case 1: # TO STEAL A ITEM
                        match(rand.randint(1,4)): 
                            case 1:
                                means_of_action = "by stealing '" + self.generateMacguffin() + "' from " + rand.choice(cities+major_locations+ minor_locations)
                            case 2:
                                means_of_action = "by stealing '" + self.generateMacguffin() + "' from " + rand.choice(npcs)
                            case 3:
                                means_of_action = "by stealing '" + self.generateMacguffin() + "' from " + local_leader
                            case 4:
                                means_of_action = "by stealing '" + self.generateMacguffin() + "' from the " + rand.choice(list(self.race_list.keys()))
                    case 2: #To steal people
                        match(rand.randint(1,6)):
                            case 1:
                                means_of_action = "by kidnaping people"
                            case 2:
                                means_of_action = "by kidnaping people from " + rand.choice(cities)
                            case 3:
                                means_of_action = "by kidnaping people from " + rand.choice(minor_locations)
                            case 4:
                                means_of_action = "by kidnaping " + rand.choice(npcs)
                            case 5:
                                means_of_action = "by kidnaping leader of " + rand.choice(cities)
                            case 6:
                                means_of_action = "by kidnaping leader of " + rand.choice(minor_locations)
                    
            case 2: #TO KILL/SACRIFICE
                match(rand.randint(1,2)):
                    case 1: #KILL
                        match(rand.randint(1,6)):
                            case 1:
                                means_of_action = "by killing all " + rand.choice(list(self.race_list.keys()))
                            case 2:
                                means_of_action = "by killing all inhabitants of " + rand.choice(cities+major_locations+ minor_locations)
                            case 3:
                                means_of_action = "by killing " + (rand.choice(npcs))
                            case 4:
                                means_of_action = "by killing a god"
                            case 5:
                                means_of_action = "by killing the legendary " + rand.choice(self.general_details["Monsters"]) + "(s)"
                            case 6:
                                means_of_action = "by killing all inhabitants of " + area_name
                    case 2: #sacrifice
                        match(rand.randint(1,7)):
                            case 1:
                                means_of_action = "by sacrificing all " + rand.choice(list(self.race_list.keys()))
                            case 2:
                                means_of_action = "by sacrificing all inhabitants of " + rand.choice(cities+major_locations+ minor_locations)
                            case 3:
                                means_of_action = "by killing all inhabitants of " + area_name
                            case 4:
                                means_of_action = "by sacrificing " + (rand.choice(npcs))
                            case 5:
                                means_of_action = "by sacrificing a god"
                            case 6:
                                means_of_action = "by sacrificing the legendary " + rand.choice(self.general_details["Monsters"]) + "(s)"
                            case 7:
                                means_of_action = "by sacrificing the legendary " + self.generateMacguffin()
            case 3: #Conquer/Invade
                match(rand.randint(1,2)):
                    case 1: #Conquer
                        match(rand.randint(1,2)):
                            case 1:
                                means_of_action = "by conquering " + area_name
                            case 2:
                                means_of_action = "by conquering " + rand.choice(cities+major_locations+ minor_locations)
                    case 2: #Invade
                        match(rand.randint(1,2)):
                            case 1:
                                means_of_action = "by invading neighboring region/nation" 
                            case 2:
                                means_of_action = "by invading " + rand.choice(cities+major_locations+ minor_locations)
            case 3: #Destroy
                match(rand.randint(1,4)):
                    case 1:
                        means_of_action = "by spreading Plague across the lands"
                    case 2:
                        means_of_action = "by driving out all residents out of " + area_name + " through action"
                    case 2:
                        means_of_action = "by driving out all residents out of " + rand.choice(cities+major_locations+ minor_locations) + " through action"
                    case 4:
                        means_of_action = "by reducing " + area_name + " to rubble"
                    case 5:
                        means_of_action = "by reducing " + rand.choice(cities+major_locations+ minor_locations) + " to rubble"
            case 4: #To subvert
                match(rand.randint(1,3)):
                    case 1:
                        means_of_action = "by subverting the hierachy of " +area_name
                    case 2:
                        means_of_action = "by subverting the hierachy of " +rand.choice(cities+major_locations+ minor_locations)
                    case 3:
                        means_of_action = "by subverting a religious hierachy"
            case 5: #Politics
                match(rand.randint(1,6)):
                    case 1:
                        means_of_action = "by betraying the leader of " +area_name
                    case 2:
                        means_of_action = "by betraying the leader of " +rand.choice(cities+major_locations+ minor_locations)
                    case 3:
                        means_of_action = "by starting a rebellion/revolution in " + area_name
                    case 4:
                        means_of_action = "by starting a rebellion/revolution in " + rand.choice(cities+major_locations+ minor_locations)
                    case 5:
                        means_of_action = "by starting a commiting acts of terrorism in " + area_name
                    case 6:
                        means_of_action = "by starting a commiting acts of terrorism in " + rand.choice(cities+major_locations+ minor_locations)

        
        return Goal + " " +  means_of_action       

    def generatePoliticalSystem(self):
        system = ""
        title = ""
        home = ""
        choice = rand.randint(1,6)
        options = []
        match(choice):
            case 1:
                system = "Authoritarian/Dictator"
                royal_option = rand.choice(["King/Queen","Prince/Princess","Duke/Duchess","Marquess/Marchioness","Earl/Countess","Viscount/Viscountess","Baron,Baroness"])
                options.append(royal_option)
                options += ["Dictator","Emperor"]
            case 2:
                system = "Theocratic Authoritarian"
                royal_option = rand.choice(["King/Queen","Prince/Princess","Duke/Duchess","Marquess/Marchioness","Earl/Countess","Viscount/Viscountess","Baron,Baroness"])
                options.append(royal_option)
                options +=  ["Cleric","Elder","Pontiff","Priest","Deacon","Emperor"]
            case 3:
                system = "Communism"
                title = ["Chancellor of the People"]
            case 4:
                system = "Military Dictatorship"
                royal_option = rand.choice(["King/Queen","Prince/Princess","Duke/Duchess","Marquess/Marchioness","Earl/Countess","Viscount/Viscountess","Baron,Baroness"])
                options.append(royal_option)
                options +=  ["General","Dictator","Emperor"]
            case 5:
                system = "Democracy"
                options =  ["Council Head","Lead Parlimentarian","Chancellor","Senator","Elder"]
            case 6:
                system = "Monarchy"
                options =  ["King/Queen","Prince/Princess","Duke/Duchess","Marquess/Marchioness","Earl/Countess","Viscount/Viscountess","Baron,Baroness"]
                
        if len(options) != 0:
            title = rand.choice(options)

        if choice in [1,4,6]: # absolute rules
            home = self.generateLOI(False,False)
        elif choice == 2:
            diety = (title.partition("of "))
            home = self.generateReligiousBuildingName(diety= diety[2] )
        elif choice == 5:
            home = (self.generateBuilding("Notable_Housing"))[0]

        return system,title,home



