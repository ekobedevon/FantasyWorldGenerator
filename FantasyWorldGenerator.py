import PySimpleGUI as sg
import NPC
import Building
import Generator

MASTER_GENERATOR =Generator.generator()
test_npc = NPC.NPC(MASTER_GENERATOR)
for x in range(0,20):
    temp = Building.Building(gen=MASTER_GENERATOR)
    dict_temp = temp.__dict__()
    print(dict_temp)


exit = 0;

while(exit):
    layout = test_npc.createDisplayA()
    layout += [[sg.Button("New NPC",key="--NewNPC--"),sg.Button("Exit",key="--EXIT--")]]
    window = sg.Window('Window that stays open', layout)
    events, values = window.read()
    if events != None:
        if "--EXIT--" in events:
            exit = 0
            window.close()
        elif "--NewNPC--" in events:
            test_npc = NPC.NPC(MASTER_GENERATOR)
            window.close()
    else:
        exit = 0
        window.close()







