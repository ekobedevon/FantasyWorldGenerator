import PySimpleGUI as sg
import os
import NPC
import Building
import Generator
import OutputObsidian as OutOD
sg.theme('DarkTeal9')
BASE_PATH = os.getcwd()
MASTER_GENERATOR =Generator.generator()

#STYLE STUFF
d_f_b = (10,1) #DEFAULT BUTTON SIZE

#create Export Folder if not already existing
if "Export" not in os.listdir():
    os.mkdir("Export")

current_displayed = None
exit =1;
layout=[[]]

while(exit): # loop until exit is changed
    button_layout = [[sg.Button("New NPC",key="--NewNPC--",size=d_f_b)],[sg.Button("New Building",key="--NewBuild--",size=d_f_b)],[sg.Button("Exit",key="--EXIT--",size=d_f_b)]]
    if current_displayed != None:
        button_layout.append([sg.Button("Export",key="--Export--",size = d_f_b)])
    layout= [[sg.Column(layout),sg.Column(button_layout)]]
    window = sg.Window("Abnormal World Generator",layout)
    events,values = window.read()
    match(events):
        case "--EXIT--": # exit program
            exit = 0
            window.close()
        case "--NewNPC--": # generate a new NPC
            current_displayed = NPC.NPC(MASTER_GENERATOR)
            layout = current_displayed .createDisplay()
            window.close()
        case "--NewBuild--": # generate a new building
            current_displayed  = Building.Building(MASTER_GENERATOR)
            layout = current_displayed .createDisplay();
            window.close()
        case "--Export--": #export the currently displayed information
            os.chdir("./Export")
            path = os.getcwd()
            #OutOD.export(current_displayed) # export the displayer info
            window.close()
            layout = [[sg.Text("Exported to " + path,justification="center",size=(50,1))],[sg.Text("Returning to main menu...",justification="center",size=(50,1))],[sg.Column([[sg.Button("OK",size=d_f_b)]],justification='center')]]
            window = sg.Window("Abnormal World Generator",layout)
            window.read()
            window.close()
            layout = [[]]
            current_displayed = None
            os.chdir(BASE_PATH)
    if events == None:
        exit = 0
        window.close()








