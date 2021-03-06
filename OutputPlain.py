import os
from random import randint
import Building
import City
import NPC
import Region
import Continent
import Generator
extra = ""
tags = {}
tags["c"] = "City_"
tags["b"] = "Building_"
tags["r"] = "Region_"
tags["p"] = "Pantheon_"
tags["ct"] = "Continent_"

"""NOTE: Obsidian uses paths to distinguish unique names, so in the future as world gen gets bigger, it might be needed to add a process that ensures all names are unique before exporting"""

def GenerateUniqueName(file_name: str,file_set: set,file_extension: str = ""):
    while len({file_name + file_extension}.intersection(file_set)):
        file_name += hex(randint(0,15)).removeprefix("0x")#keeps adding hex values to file name unitl it is unique
    return file_name + file_extension


def export(item,gen:Generator.generator = None): #generic export to be used when item type is not stricly defined

    if type(item) == Continent.Continent:
        exportContinent(item)
    elif type(item) == Region.Region:

        exportRegion(item)
    elif type(item) == City.City:
        exportCity(item)
    elif type(item) == Building.Building:
        exportBuilding(item)
    elif type(item) == NPC.NPC:
        exportNPC(item)
        
    if item != None and gen != None:
        exportGeneralDetail(gen)
        
def exportGeneralDetail(gen:Generator.generator):
    os.mkdir("./Pantheon") # create pantheon folder
    os.chdir("./Pantheon") # enter panthon directory
    for god in list(gen.pantheon.keys()):
        file = open("Deity of "+god+".txt", 'w')
        file.write("General Details\n")
        file.write("Name: %s\n" % gen.pantheon[god])
        file.close()


def exportNPC(npc: NPC.NPC):
    file_set = set(os.listdir())
    file_name =GenerateUniqueName(npc.name,file_set,".txt")
    file = open(file_name, 'w')
    file.write("General Details:\n")
    file.write("Name: %s\n" % npc.name)
    file.write("Race: %s\n" % npc.race)
    file.write("Sex: %s\n" % npc.sex)
    file.write("Age: %s\n" % npc.age)
    file.write("Origin: %s<\n" % npc.origin)
    file.write("Profession: %s\n" % npc.profession)
    file.write("\nPersonality:\n")
    if npc.goals != "":
        file.write("Lair: %s\n" % npc.lair)
    for detail in npc.origin_details:
        file.write("%s:" % detail)
        file.write("%s\n" % npc.origin_details[detail])
    if npc.goals != "":
        file.write("\nGoals:\n")
        file.write("%s\n" % npc.goals)

    file.close()
 


def exportBuilding(building: Building.Building):
    file_set = set(os.listdir()) #get all files in director
    folder_name = building.building_name #get potential name
    folder_name = GenerateUniqueName(tags["b"]+folder_name,file_set,"") #generate unique name  for this building
    os.mkdir(folder_name) #create a folder just for the building name
    os.chdir("./"+folder_name) #enter that folder
    os.mkdir("Occupants") #create occupants folder
    file = open(folder_name.removeprefix(tags["b"]) + ".txt", 'w')
    file.write("General Info \n")
    file.write("Name: %s\n" % building.building_name)
    file.write("Building Type: %s\n" % building.building_type)
    file.write("Owner:  %s \n" % building.owner.name )
    if building.building_menu != "":
        file.write("Building Offerings:\n%s" % building.building_menu)
    file.write("Occupants \n")
    for occupant in building.occupants:
        file.write(" %s \n" % occupant.name)
    file.write("Hooks \n")
    for hook in building.hooks:
        file.write("%s \n" % hook)
    file.close()
    base = os.getcwd() #base working directory
    os.chdir("./Occupants") #write all occupants 
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
    file = open((folder_name + ".txt").removeprefix(tags["c"]), 'w')
    file.write("General Info \n")
    file.write("Name: %s\n" % city.city_name)
    file.write("City Population: %s \n" % str(city.city_pop))
    file.write("Local Leader:  %s \n" % city.city_leader.name) 
    file.write("Buildings \n")
    for building in city.buildings_list:
        file.write(" %s \n" % building.building_name)
    file.write("Wandering NPCs \n")
    for npc in city.wandering_npcs:
        file.write(" %s \n" % npc.name)
    file.write("Nearby Locations of Interest \n")
    for loi in city.LOI:
        file.write("%s \n" % loi)
    file.write("Local Hooks \n")
    for hooks in city.hooks:
        file.write("%s \n" % hooks)

    base = os.getcwd() #base working directory
    os.chdir("./Buildings")
    curDirectory = os.getcwd()
    for building in city.buildings_list:
        os.chdir(curDirectory)
        exportBuilding(building)

    os.chdir(base) #return to proper directory
    os.chdir("./Wandering NPCs")
    for npc in city.wandering_npcs:
        exportNPC(npc)
    os.chdir(base) # return to base directory

def exportRegion(region:Region.Region):
    file_set = set(os.listdir()) #get all files in director
    folder_name = region.region_name #get potential name
    folder_name = GenerateUniqueName(tags["r"] +folder_name,file_set) #generate unique name  for this building
    os.mkdir(folder_name) #create a folder just for the building name
    os.chdir("./"+folder_name) #enter that folder
    os.mkdir("Cities") #create buildings folder
    os.mkdir("Regional Powers")
    file = open((folder_name + ".txt").removeprefix(tags["r"]), 'w')
    file.write("General Info \n")
    file.write("Name: %s\n" % region.region_name)
    file.write("Population: %s\n" % int(region.population))
    if region.capital != None:
        file.write("Political System: %s\n" % region.political_system)
        file.write("Capital: %s\n" % region.capital.city_name)
        file.write("Regional Leader Leader:  %s \n" % region.political_leader.name)
    file.write("Regional Cities\n")
    for cities in region.cities:
        file.write("%s \n" % cities.city_name)
    file.write("Regional Powers\n")
    for npc in region.region_powers:
        file.write("%s \n" % npc.name)
    file.write("Major Locations of Interest \n")
    for loi in region.major_LOI:
        file.write("%s \n" % loi)
    file.write("Minor Locations of Interest \n")
    for loi in region.minor_LOI:
        file.write("%s \n" % loi)
    file.write("Regional Hooks \n")
    for hooks in region.hooks:
        file.write("%s \n" % hooks)

    base = os.getcwd() #base working directory
    os.chdir("./Cities")
    curDirectory = os.getcwd()
    for cities in region.cities:
        os.chdir(curDirectory)
        exportCity(cities)

    os.chdir(base) #return to proper directory
    os.chdir("./Regional Powers")
    for npc in region.region_powers:
        exportNPC(npc)
    
    os.chdir(base) 

def exportContinent(cont:Continent.Continent):
    file_set = set(os.listdir()) #get all files in director
    folder_name = cont.continent_name #get potential name
    folder_name = GenerateUniqueName(tags["ct"] +folder_name,file_set) #generate unique name  for this building
    os.mkdir(folder_name) #create a folder just for the building name
    os.chdir("./"+folder_name) #enter that folder
    os.mkdir("Regions") #create buildings folder
    os.mkdir("Continental Powers")
    file = open((folder_name + ".txt").removeprefix(tags["r"]), 'w')
    file.write("## General Info \n")
    file.write("**Name:** %s\n" % cont.continent_name)
    file.write("**Population:** %s\n" % int(cont.sumPop))
    if cont.capital != None:
        file.write("**Political System:** %s\n" % cont.political_system)
        file.write("**Capital:** %s\n" % cont.capital.city_name)
        file.write("**Continental Leader Leader:**  [[%s]] \n" % cont.political_leader.name)
    file.write("### Continental Regiond\n")
    for regions in cont.regions:
        file.write(" %s \n" % regions.region_name)
    file.write("### Continental Powers\n")
    for npc in cont.continent_powers:
        file.write(" %s \n" % npc.name)
    file.write("### Major Locations of Interest \n")
    for loi in cont.major_LOI:
        file.write("%s \n" % loi)
    file.write("### Minor Locations of Interest \n")
    for loi in cont.minor_LOI:
        file.write("%s \n" % loi)


    base = os.getcwd() # base working directory
    os.chdir("./Regions")
    curDirectory = os.getcwd()
    for region in cont.regions:
        os.chdir(curDirectory)
        exportRegion(region)

    os.chdir(base) # return to proper directory
    os.chdir("./Continental Powers")
    for npc in cont.continent_powers:
        exportNPC(npc)

    os.chdir(base) # return to base directory



