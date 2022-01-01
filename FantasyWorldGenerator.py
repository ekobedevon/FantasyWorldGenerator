import PySimpleGUI as sg
import os
import NPC
import Building
import City
import Region
import Continent
import Generator
import random
import time
import datetime
import OutputObsidian as OutOD
import OutputPlain as OutP
import OutputMarkdown as OutMD
import Style as s
sg.theme('DarkTeal9')
BASE_PATH = os.getcwd()
MASTER_GENERATOR =Generator.generator()
random.seed(time.time())




#STYLE STUFF
d_f_b = (10,1) #DEFAULT BUTTON SIZE
export_text = (80,1)

#create Export Folder if not already existing
if "Export" not in os.listdir():
    os.mkdir("Export")

world_name = MASTER_GENERATOR.generateWorldName() # generate a world name



#Variables used to maintina the GUI
current_displayed = None #used to hold the currently displayed element
displayed_stack = [] #used to store in order, the parent elements in order to allow layers in menu
button_menu = 1
is_visible = False
exit =1
while(exit): # loop until exit is changed
    button_layout = [[]]
    general_buttons = [[]]
    if current_displayed != None:
        export_layout = [[sg.Button("Obsidian",key="--ExportOBS--",size = d_f_b)],[sg.Button("Plain Text",key="--ExportPlain--",size = d_f_b)],[sg.Button("Markdown",key="--ExportMD--",size = d_f_b)]]
        button_layout = [[sg.Frame("Export",export_layout)]]
        layout = current_displayed.createDisplay()
    else:
        layout = [[]]
    match(button_menu): #display differen't menus based on what is being veiwed
        case 1:
            general_buttons = [[sg.Button("New NPC",key="--NewNPC--",size=d_f_b)],
                                [sg.Button("New Building",key="--NewBuild--",size=d_f_b)],
                                [sg.Button("New City",key="--NewCity--",size=d_f_b)],
                                [sg.Button("New Region",key="--NewRegion--",size=d_f_b)],
                                [sg.Button("New Continent",key="--NewCont--",size=d_f_b)],
                                [sg.Button("Exit",key="--EXIT--",size=d_f_b)]]
        case 2:
            general_buttons = [[sg.Button("Return",key="--Return--",size=d_f_b)],[sg.Button("Exit",key="--EXIT--",size=d_f_b)],[sg.Button("Main Menu",key="--Main--",size=d_f_b,visible=is_visible)]]
    button_layout.append([sg.Frame("General",general_buttons)])
    layout= [[sg.Column(layout),sg.Column(button_layout)]]
    window = sg.Window("Abnormal World Generator",layout)
    events,values = window.read()
    if events != None:
        if "_" not in events:
            match(events):
                case "--EXIT--": # exit program
                    exit = 0
                    window.close()
                case "--NewNPC--": # generate a new NPC
                    current_displayed = NPC.NPC(MASTER_GENERATOR)
                    window.close()
                case "--NewBuild--": # generate a new building
                    current_displayed  = Building.Building(MASTER_GENERATOR)
                    layout = current_displayed.createDisplay()
                    window.close()
                case "--NewCity--": #generate a new city
                    current_displayed = City.City(MASTER_GENERATOR)
                    window.close()
                case "--NewRegion--":
                    current_displayed = Region.Region(MASTER_GENERATOR)
                    window.close()
                case "--NewCont--":
                        current_displayed = Continent.Continent(MASTER_GENERATOR)
                        window.close()
                case "--Return--": #go up one layer
                    current_displayed = displayed_stack.pop() # pop last display of stack
                    window.close()
                case "--Main--":
                    displayed_stack = []
                    window.close()
                case "--ExportOBS--": #export the currently displayed information
                    os.chdir("./Export")
                    if (world_name+"_Obsidian") not in os.listdir():
                        os.mkdir(world_name+"_Obsidian")
                    os.chdir("./"+world_name+"_Obsidian")
                    path_current = os.getcwd()
                    OutOD.export(current_displayed,MASTER_GENERATOR) # export the displayer info
                    os.chdir(path_current)
                    if "Pantheon" not in os.listdir():
                        OutOD.exportGeneralDetail(MASTER_GENERATOR)
                    window.close()
                    layout = [[sg.Text("Exported to " + path_current,justification="center",size=export_text)],[sg.Text("Returning to main menu...",justification="center",size=export_text)],[sg.Column([[sg.Button("OK",size=d_f_b)]],justification='center')]]
                    window = sg.Window("Abnormal World Generator",layout)
                    window.read()
                    window.close()
                    current_displayed = None
                    is_visible = True # set return button as visible
                    os.chdir(BASE_PATH)
                case "--ExportPlain--": #export the currently displayed information
                    os.chdir("./Export")
                    if (world_name+"_Plain Text") not in os.listdir():
                        os.mkdir(world_name+"_Plain Text")
                    os.chdir("./"+world_name+"_Plain Text")
                    OutP.export(current_displayed) # export the displayer info
                    window.close()
                    path_current = os.getcwd()
                    layout = [[sg.Text("Exported to " + path_current,justification="center",size=export_text)],[sg.Text("Returning to main menu...",justification="center",size=export_text)],[sg.Column([[sg.Button("OK",size=d_f_b)]],justification='center')]]
                    window = sg.Window("Abnormal World Generator",layout)
                    window.read()
                    window.close()
                    current_displayed = None
                    is_visible = True # set return button as visible
                    os.chdir(BASE_PATH)
                case "--ExportMD--": #export the currently displayed information
                    os.chdir("./Export")
                    if (world_name+"_Mark Down") not in os.listdir():
                        os.mkdir(world_name+"_Mark Down")
                    os.chdir("./"+ world_name+"_Mark Down")
                    OutMD.export(current_displayed) # export the displayer info
                    window.close()
                    path_current = os.getcwd()
                    layout = [[sg.Text("Exported to " + path_current,justification="center",size=export_text)],[sg.Text("Returning to main menu...",justification="center",size=export_text)],[sg.Column([[sg.Button("OK",size=d_f_b)]],justification='center')]]
                    window = sg.Window("Abnormal World Generator",layout)
                    window.read()
                    window.close()
                    current_displayed = None
                    is_visible = True # set return button as visible
                    os.chdir(BASE_PATH)
        else:
            if "_cont" in events:
                b_index = (events.removesuffix("_cont"))
                if "_region" in events:
                    b_index = int(b_index.removesuffix("_region")) # the int of the building clicked
                    displayed_stack.append(current_displayed)
                    current_displayed = current_displayed.regions[b_index]
                else:
                    b_index = int(b_index.removesuffix("_npc"))
                    displayed_stack.append(current_displayed)
                    current_displayed = current_displayed.continent_powers[b_index]
                window.close()
            elif "_region" in events:
                b_index = (events.removesuffix("_region"))
                if "_city" in events:
                    b_index = int(b_index.removesuffix("_city")) # the int of the building clicked
                    displayed_stack.append(current_displayed)
                    current_displayed = current_displayed.cities[b_index]
                else:
                    b_index = int(b_index.removesuffix("_npc"))
                    displayed_stack.append(current_displayed)
                    current_displayed = current_displayed.region_powers[b_index]
                window.close()
            elif "_city" in events:
                b_index = (events.removesuffix("_city")) # the int of the building clicked
                displayed_stack.append(current_displayed) # push displayed onto stack
                if "_building" in events:
                    b_index = int(b_index.removesuffix("_building"))
                    current_displayed = current_displayed.buildings_list[b_index]
                else:
                    b_index = int(b_index.removesuffix("_npc"))
                    current_displayed = current_displayed.wandering_npcs[b_index]
                window.close()
            elif "_building" in events:
                displayed_stack.append(current_displayed)
                b_index = int(events.removesuffix("_building"))
                current_displayed = current_displayed.occupants[b_index]
                window.close()
            


    if len(displayed_stack) != 0:
        button_menu = 2 #display menu with back options
    else:
        is_visible = False
        button_menu = 1 #display menu with generate options


    if events == None:
        exit = 0
        window.close()



