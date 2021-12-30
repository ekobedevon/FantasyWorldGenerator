import os
from random import randint
import Building
import City
import NPC
import Region
import Generator
extra = ""
tags = {}
tags["c"] = "[City]"
tags["b"] = "[Building]"
tags["r"] = "[Region]"


"""NOTE: Obsidian uses paths to distinguish unique names, so in the future as world gen gets bigger, it might be needed to add a process that ensures all names are unique before exporting"""

def GenerateUniqueName(file_name: str,file_set: set,file_extension: str = ""):
    while len({file_name + file_extension}.intersection(file_set)):
        file_name += hex(randint(0,15)).removeprefix("0x")#keeps adding hex values to file name unitl it is unique
    return file_name + file_extension


def export(item): #generic export to be used when item type is not stricly defined
    if type(item) == Region.Region:
        exportRegion(item)
    elif type(item) == City.City:
        exportCity(item)
    elif type(item) == Building.Building:
        exportBuilding(item)
    elif type(item) == NPC.NPC:
        exportNPC(item)

def exportGeneralDetail(gen:Generator.generator):
    os.mkdir("./Pantheon") # create pantheon folder
    os.chdir("./Pantheon") # enter panthon directory
    for domain in list(gen.pantheon.keys()):
        file = open("Diety of "+domain+".MD" 'w')
        file.write("## General Details<br>\n")
        file.write("**Name:** %s<br>\n" % gen.pantheon[domain])
        file.close()

def getDomain(string:str): # get the domain of the god
    temp = string.partition("Diety")
    domain = temp[1]+temp[2]
    domain = domain.removesuffix(" domain") #remove the domain
    domain = domain.replace("the ","",1) # remove "the"
    return domain  


def exportNPC(npc: NPC.NPC):
    file_set = set(os.listdir())
    file_name =GenerateUniqueName(npc.name,file_set,".MD")
    file = open(file_name, 'w')
    file.write("## General Details<br>\n")
    file.write("**Name:** %s<br>\n" % npc.name)
    file.write("**Race:** %s<br>\n" % npc.race)
    file.write("**Sex:** %s<br>\n" % npc.sex)
    file.write("**Age:** %s<br>\n" % npc.age)
    file.write("**Origin:** %s<br>\n" % npc.origin)
    file.write("**Profession:** %s<br>\n" % npc.profession)
    if npc.goals != "":
        file.write("**Lair:** %s<br>\n" % npc.lair)
    file.write("## Personality<br>\n")
    for detail in npc.origin_details:
        file.write("**%s:**" % detail)
        file.write("%s<br>\n" % npc.origin_details[detail])
    if npc.goals != "":
        file.write("## Goals <br>\n")
        file.write("%s<br>\n" % npc.goals)
    file.close()

def exportBuilding(building: Building.Building):
    file_set = set(os.listdir()) #get all files in director
    folder_name = building.building_name #get potential name
    folder_name = GenerateUniqueName(tags["b"]+folder_name,file_set,"") #generate unique name  for this building
    os.mkdir(folder_name) #create a folder just for the building name
    os.chdir("./"+folder_name) #enter that folder
    os.mkdir("Occupants") #create occupants folder
    file = open(folder_name.removeprefix(tags["b"]) + ".MD", 'w')
    file.write("## General Info <br>\n")   
    file.write("**Name:** %s<br>\n" % building.building_name)
    file.write("**Building Type:** %s<br>\n" % building.building_type)
    file.write("**Owner:**  %s <br>\n" % building.owner.name ) 
    file.write("### Occupants <br>\n")
    for occupant in building.occupants:
        file.write(" %s <br>\n" % occupant.name)
    file.write("### Hooks <br>\n")
    for hook in building.hooks:
        file.write("%s <br>\n" % hook)
    file.close()
    base = os.getcwd() #base working directory
    os.chdir("./Occupants") #write all occupants 
    exportNPC(building.owner)
    for occupant in building.occupants:
        exportNPC(occupant)

    os.chdir(base) 


def exportCity(city:City.City):
    file_set = set(os.listdir()) #get all files in director
    folder_name = city.city_name #get potential name
    folder_name = GenerateUniqueName(tags["c"] +folder_name,file_set) #generate unique name  for this building
    os.mkdir(folder_name) #create a folder just for the building name
    os.chdir("./"+folder_name) #enter that folder
    os.mkdir("Buildings") #create buildings folder
    os.mkdir("Wandering NPCs")
    file = open((folder_name + ".MD").removeprefix(tags["c"]), 'w')
    file.write("## General Info <br>\n")
    file.write("**Name:** %s<br>\n" % city.city_name)
    file.write("**City Population**: %s<br> \n" % str(city.city_pop))
    file.write("**Local Leader:**  %s <br>\n" % city.city_leader.name) 
    file.write("### Buildings <br>\n")
    for building in city.buildings_list:
        file.write(" %s <br>\n" % building.building_name)
    file.write("### Wandering NPCs <br>\n")
    for npc in city.wandering_npcs:
        file.write(" %s <br>\n" % npc.name)
    file.write("### Nearby Locations of Interest <br>\n")
    for loi in city.LOI:
        file.write("%s <br>\n" % loi)
    file.write("### Local Hooks <br>\n")
    for hooks in city.hooks:
        file.write("%s <br>\n" % hooks)

    base = os.getcwd() # base working directory
    os.chdir("./Buildings")
    curDirectory = os.getcwd()
    for building in city.buildings_list:
        os.chdir(curDirectory)
        exportBuilding(building)

    os.chdir(base) # return to proper directory
    os.chdir("./Wandering NPCs")
    exportNPC(city.city_leader)
    for npc in city.wandering_npcs:
        exportNPC(npc)

    os.chdir(base) 

def exportRegion(region:Region.Region):
    file_set = set(os.listdir()) #get all files in director
    folder_name = region.region_name #get potential name
    folder_name = GenerateUniqueName(tags["r"] +folder_name,file_set) #generate unique name  for this building
    os.mkdir(folder_name) #create a folder just for the building name
    os.chdir("./"+folder_name) #enter that folder
    os.mkdir("Cities") #create buildings folder
    os.mkdir("Regional Powers")
    file = open((folder_name + ".MD").removeprefix(tags["r"]), 'w')
    file.write("## General Info <br>\n")
    file.write("**Name:** %s<br>\n" % region.region_name)
    file.write("**Population:** %s<br>\n" % int(region.population))
    if region.capital != None:
        file.write("**Political System:** %s<br>\n" % region.political_system)
        file.write("**Capital:** %s<br>\n" % region.capital.city_name)
        file.write("**Regional Leader Leader:**  %s <br>\n" % region.political_leader.name)
    file.write("### Regional Cities<br>\n")
    for cities in region.cities:
        file.write(" %s <br>\n" % cities.city_name)
    file.write("### Regional Powers<br>\n")
    for npc in region.region_powers:
        file.write(" %s <br>\n" % npc.name)
    file.write("### Major Locations of Interest <br>\n")
    for loi in region.major_LOI:
        file.write("%s <br>\n" % loi)
    file.write("### Minor Locations of Interest <br>\n")
    for loi in region.minor_LOI:
        file.write("%s <br>\n" % loi)
    file.write("### Regional Hooks <br>\n")
    for hooks in region.hooks:
        file.write("%s <br>\n" % hooks)

    base = os.getcwd() # base working directory
    os.chdir("./Cities")
    curDirectory = os.getcwd()
    for cities in region.cities:
        os.chdir(curDirectory)
        exportCity(cities)

    os.chdir(base) # return to proper directory
    os.chdir("./Regional Powers")
    for npc in region.region_powers:
        exportNPC(npc)

    os.chdir(base) 
    
    



