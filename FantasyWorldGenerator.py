import PySimpleGUI as sg
import NPC
import Building
import Generator
sg.theme('DarkTeal9')
MASTER_GENERATOR =Generator.generator()

exit =1;
layout=[[]]

while(exit):
    button_layout = [[sg.Button("New NPC",key="--NewNPC--")],[sg.Button("New Building",key="--NewBuild--")],[sg.Button("Exit",key="--EXIT--")]]
    layout= [[sg.Column(layout),sg.Column(button_layout)]]
    window = sg.Window("Abnormal World Generator",layout)
    events,values = window.read()
    if events != None:
        if "--EXIT--" in events:
            exit = 0
            window.close()
        elif "--NewNPC--" in events:
            layout =[[]]
            test_npc = NPC.NPC(MASTER_GENERATOR)
            layout = test_npc.createDisplay()
            window.close()
        elif "--NewBuild--" in events:
            layout =[[]]
            test_building = Building.Building(MASTER_GENERATOR)
            layout = test_building.createDisplay();
            window.close()
    else:
        exit = 0
        window.close()








