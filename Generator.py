import json as js
import os
import random as rand
import math

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
    if len(race_dict["Settings"]) != 2: #if settings doesn't have current minimum settings
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
                print(race + "is not in a valid format, checking settings file in race folder")
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



    def generateRace(self):
        if len(self.race_list) != None:
            list_keys = list(self.race_list.keys())
            return rand.choice(list_keys)


    def generateName(self,race: str, sex: str = ""):
        """Given a string, generate a name based of settings"""
        name = ""
        match len(self.race_list[race]):
            case 1:
                print("Not enough arguments")
            case 2:
                print("Non gendered names to come")
            case 3:# races with no last names 
                if sex == "M" or sex == "F":
                    name = rand.choice(self.race_list[race][race+"_"+sex])
            case 4: #races with simple last names
                if sex == "M" or sex == "F":
                    name = rand.choice(self.race_list[race][race+"_"+sex])
                name = name + " " + rand.choice(self.race_list[race][race+"_Last"])
            case 5: #races with complex last names(2 parts)
                if sex == "M" or sex == "F":
                    name = rand.choice(self.race_list[race][race+"_"+sex])
                name = name + " of " + rand.choice(self.race_list[race][race+"_Pre"])  + " " + rand.choice(self.race_list[race][race+"_Post"])
        return name

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

    def generateReligiousBuildingName(self):
        name = rand.choice(self.building_names["Worship_Titles"]) + " of [" + rand.choice(self.general_details["Domains"]) + "] God"
        return name

    def generateBuilding(self,building_type: str = None,location: str = ""):
        building_name = ""
        owner_proffesion = ""
        suffix = ""
        if location != "":
            suffix = " of " + location 
        if building_type == None or building_type not in self.building_type: #if their is no building type or if the building type is not valid
            #print("No valid building type given, generating random building name")
            building_type = rand.choice(self.building_types) # generate a building type
        match(building_type):
            case "Shops":
                building_name = self.generateBuildingName()
                owner_proffesion = "Owner and Operator of " + building_name
            case "Tavern":
                building_name = self.generateTavernName()
                owner_proffesion = "Owner and Operator of " + building_name
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
                owner_proffesion = "Owner and Operator of " + building_name
            case "Religious":
                building_name = self.generateReligiousBuildingName()
                owner_proffesion = "Member of " + building_name

        return building_name, owner_proffesion,building_type
            
    def generateMacguffin(self,item_type: str = None):
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

    def generateHook(self,quest_giver: str = None,target: str = None,location: str = None, reward: str = None,Q_type: int = 1):
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
        
        if rand.randint(0,1) and Q_type == 1:
            party_verb = rand.choice(self.quest_details["Kill_Synonyms"])
            if target == None: # if no target given, generate a monster to target
                target = rand.choice(self.general_details["Monsters"]) + "(s)"
            objective_verb = rand.choice(self.quest_details["Oppresive_synonyms"])
            hook = quest_giver + " wants to hire the party to " + party_verb + " the " + target + " that have been " + objective_verb + " the " + location + " and will pay them with a " + reward + "."
        else:
            party_verb = rand.choice(self.quest_details["Find_Synonyms"])
            guide_item = rand.choice(self.quest_details["Map_Alternates"])
            
            hook = "The Party " + party_verb + " a " + guide_item + " that leads them to " + location + ", the " + guide_item + " leads them to believe there is a " + reward + " located somewhere inside."
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
        print("")
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
        match(rand.randint(0,8)):
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
            case 5,6,7,8:
                name = b_type+ " of " + owner
        return name

    def generateCityName(self):
        return rand.choice(self.city_details["Name_Start"]) + rand.choice(self.city_details["Name_Endings"]).lower()