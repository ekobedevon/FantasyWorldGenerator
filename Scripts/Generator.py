import json as js
import os


class generator(): # create a generator object
     #Class Variables
    race_list = {} # a dictionary of all the races
    #create a generator object that stores all the data at the start
    def __init__(self) -> None: 
        os.chdir("Json_Files\Races")
        race_fileList = os.listdir("./") # all races in the files
        for race in race_fileList:
            data = initialize_race(race) 
            if type(data) != type(1): #if the data type is not an int
                self.race_list[race] = data # store in data
            else:
                print(race + "is not in a valid format, checking settings file in race folder");


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

