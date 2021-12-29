
import PySimpleGUI as sg
import os
import NPC
import Building
import City
import Generator
import random
import time
import OutputObsidian as OutOD
sg.theme('DarkTeal9')
BASE_PATH = os.getcwd()
MASTER_GENERATOR =Generator.generator()
random.seed(time.time())



#STYLE STUFF
d_f_b = (10,1) #DEFAULT BUTTON SIZE

#create Export Folder if not already existing
if "Export" not in os.listdir():
    os.mkdir("Export")

current_displayed = None #used to hold the currently displayed element
displayed_stack = [] #used to store in order, the parent elements in order to allow layers in menu

#case
button_menu = 1

"""layout=[[]]
button_layout = [[sg.Button("New NPC",key="--NewNPC--",size=d_f_b)],[sg.Button("New Building",key="--NewBuild--",size=d_f_b)],[sg.Button("New City",key="--NewCity--",size=d_f_b)],[sg.Button("Exit",key="--EXIT--",size=d_f_b)]]
    


temp_city = City.City(MASTER_GENERATOR)
layout = temp_city.createDisplay()
layout= [[sg.Column(layout=layout)]]
window = sg.Window("test",layout)
events, value = window.read()
window.close()"""

layout=[[]]
is_visible = False



exit =1;
while(exit): # loop until exit is changed
    match(button_menu): #display differen't menus based on what is being veiwed
        case 1:
            button_layout = [[sg.Button("New NPC",key="--NewNPC--",size=d_f_b)],[sg.Button("New Building",key="--NewBuild--",size=d_f_b)],[sg.Button("New City",key="--NewCity--",size=d_f_b)],[sg.Button("Exit",key="--EXIT--",size=d_f_b)]]
        case 2:
            button_layout = [[sg.Button("Return",key="--Return--",size=d_f_b)],[sg.Button("Exit",key="--EXIT--",size=d_f_b)],[sg.Button("Main Menu",key="--Main--",size=d_f_b,visible=is_visible)]]
    if current_displayed != None:
        button_layout.append([sg.Button("Export",key="--Export--",size = d_f_b)])
        layout = current_displayed.createDisplay()
    else:
        layout = [[]]
    layout= [[sg.Column(layout),sg.Column(button_layout)]]
    window = sg.Window("Abnormal World Generator",layout)
    events,values = window.read()
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
            case "--Return--": #go up one layer
                current_displayed = displayed_stack.pop() # pop last display of stack
                window.close()
            case "--Main--":
                displayed_stack = []
                window.close()
            case "--Export--": #export the currently displayed information
                os.chdir("./Export")
                path = os.getcwd()
                OutOD.export(current_displayed) # export the displayer info
                window.close()
                layout = [[sg.Text("Exported to " + path,justification="center",size=(50,1))],[sg.Text("Returning to main menu...",justification="center",size=(50,1))],[sg.Column([[sg.Button("OK",size=d_f_b)]],justification='center')]]
                window = sg.Window("Abnormal World Generator",layout)
                window.read()
                window.close()
                current_displayed = None
                is_visible = True # set return button as visible
                os.chdir(BASE_PATH)
    else:
        if "_city" in events:
            b_index = int(events.removesuffix("_city")) # the int of the building clicked
            displayed_stack.append(current_displayed) # push displayed onto stack
            current_displayed = current_displayed.buildings_list[b_index]
            window.close()


    if len(displayed_stack) != 0:
        button_menu = 2 #display menu with back options
    else:
        is_visible = False
        button_menu = 1 #display menu with generate options


    if events == None:
        exit = 0
        window.close()



