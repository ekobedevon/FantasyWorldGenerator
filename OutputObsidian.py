import os
from random import randint
import Building
import NPC

"""NOTE: Obsidian uses paths to distinguish unique names, so in the future as world gen gets bigger, it might be needed to add a process that ensures all names are unique before exporting"""

def GenerateUniqueName(file_name: str,file_set: set,file_extension: str = ""):
    while len({file_name + file_extension}.intersection(file_set)):
        file_name += hex(randint(0,15)).removeprefix("0x")#keeps adding hex values to file name unitl it is unique
    return file_name


def export(item): #generic export to be used when item type is not stricly defined
    if type(item) == Building.Building:
        exportBuilding(item)
    if type(item) == NPC.NPC:
        exportNPC(item)


def exportNPC(npc: NPC.NPC):
    file_set = set(os.listdir())
    file_name =GenerateUniqueName(npc.name,file_set,".MD")
    file = open(file_name, 'w')
    file.write("**Name:** %s<br>\n" % npc.name)
    file.write("**Race:** %s<br>\n" % npc.race)
    file.write("**Sex:** %s<br>\n" % npc.sex)
    file.write("**Age:** %s<br>\n" % npc.age)
    file.write("**Profession:** %s<br>\n" % npc.profession)
    file.close()

def exportBuilding(building: Building.Building, parentfolder = ""):
    file_set = set(os.listdir()) #get all files in director
    folder_name = building.building_name #get potential name
    folder_name = GenerateUniqueName(folder_name,file_set) #generate unique name  for this building
    os.mkdir(folder_name) #create a folder just for the building name
    os.chdir("./"+folder_name) #enter that folder
    os.mkdir("Occupants") #create occupants folder
    file = open(building.building_name + ".MD", 'w')
    file.write("## General Info <br>\n")
    file.write("**Name:** %s<br>\n" % building.building_name)
    file.write("**Building Type:** %s<br>\n" % building.building_type)
    file.write("**Owner:** [[%s]] <br>\n" % building.owner.name) 
    file.write("### Occupants <br>\n")
    for occupant in building.occupants:
        file.write("[[%s]] <br>\n" % occupant.name)
    file.write("### Hooks <br>\n")
    for hook in building.hooks:
        file.write("%s <br>\n" % hook)
    file.close()
    os.chdir("./Occupants") #write all occupants 
    exportNPC(building.owner)
    for occupant in building.occupants:
        exportNPC(occupant)
    
    

#  + Object 



