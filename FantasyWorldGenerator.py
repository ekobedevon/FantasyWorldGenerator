import PySimpleGUI as sg
import os
import NPC
import Building
import Generator
import OutputObsidian as OutOD
sg.theme('DarkTeal9')
BASE_PATH = os.getcwd()
MASTER_GENERATOR =Generator.generator()
"""os.chdir("./Export")
temp  = Building.Building(MASTER_GENERATOR)
OutOD.export(temp)"""

current_displayed = None

exit =1;
layout=[[]]

while(exit):
    button_layout = [[sg.Button("New NPC",key="--NewNPC--")],[sg.Button("New Building",key="--NewBuild--")],[sg.Button("Exit",key="--EXIT--")]]
    if current_displayed != None:
        button_layout.append([sg.Button("Export",key="--Export--")])
    layout= [[sg.Column(layout),sg.Column(button_layout)]]
    window = sg.Window("Abnormal World Generator",layout)
    events,values = window.read()
    if events != None:
        if "--EXIT--" in events:
            exit = 0
            window.close()
        elif "--NewNPC--" in events:
            current_displayed = NPC.NPC(MASTER_GENERATOR)
            layout = current_displayed .createDisplay()
            window.close()
        elif "--NewBuild--" in events:
            current_displayed  = Building.Building(MASTER_GENERATOR)
            layout = current_displayed .createDisplay();
            window.close()
        elif "--Export--" in events: #export the currently displayed information
            os.chdir("./Export")
            path = os.getcwd()
            OutOD.export(current_displayed) # export the displayer info
            window.close()
            layout = [[sg.Text("Exported to " + path,justification="center")],[sg.Text("Returning to main menu...")],[sg.Button("OK")]]
            window = sg.Window("Abnormal World Generator",layout)
            window.read()
            window.close()
            layout = [[]]
            current_displayed = None
            os.chdir(BASE_PATH)
    else:
        exit = 0
        window.close()








