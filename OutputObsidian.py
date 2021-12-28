import os
import Building
import NPC

"""NOTE: Obsidian uses paths to distinguish unique names, so in the future as world gen gets bigger, it might be needed to add a process that ensures all names are unique before exporting"""

def export(item):
    if type(item) == Building.Building:
        exportBuilding(item)
    if type(item) == NPC.NPC:
        exportNPC(item)




def exportNPC(npc: NPC.NPC):
    file = open(npc.name + ".MD", 'w')
    file.write("**Name:** %s<br>\n" % npc.name)
    file.write("**Race:** %s<br>\n" % npc.race)
    file.write("**Sex:** %s<br>\n" % npc.sex)
    file.write("**Age:** %s<br>\n" % npc.age)
    file.write("**Profession:** %s<br>\n" % npc.profession)
    file.close()

def exportBuilding(building: Building.Building, parentfolder = ""):
    os.mkdir(building.building_name) #create a folder just for the building name
    os.chdir("./"+building.building_name) #enter that folder
    os.mkdir("Occupants")
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
    os.chdir("./Occupants")
    exportNPC(building.owner)
    for occupant in building.occupants:
        exportNPC(occupant)
    
    

#  + Object 



