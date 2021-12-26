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
    os.chdir("Json_Files\Buildings") # set to building directory
    building_fileList = os.listdir("./")
    building_name_details = {}
    for file_name in building_fileList:
        file = open(file_name)
        data = js.load(file)
        building_name_details[file_name.removesuffix(".json")] = data
    return building_name_details

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
    general_details = {} #details that might be used between multiple generators
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

    def generateChurchName(self):
        name = rand.choice(self.building_names["Worship_Titles"]) + " of [" + rand.choice(self.general_details["Domains"]) + "] God"
        return name




