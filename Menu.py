import PySimpleGUI as sg
import json as js

def createMenu(settings:dict):
    event = []
    values = []
    while(True):
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            break
        else:
            CB_layout = [[sg.Column([[sg.Text("Export Pantheon")]]),sg.Column([[sg.CB("",default=settings["Export Pantheon"],key="--ExportPanth--")]])]]
            menu_layout = [[sg.Text('Theme Browser')], # theme layout
                        [sg.Text("Current Theme: " +settings["Current Theme"])],
                        [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)]]
            layout = [[sg.Column(CB_layout),sg.Column(menu_layout),sg.Button('Exit')]]
            window = sg.Window("TEST",layout=layout) # create window
            event,values = window.read() # read in events
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            elif '-LIST-' in event: #if the theme is changed
                sg.theme(values['-LIST-'][0])
                theme = values['-LIST-'][0]
                settings["Current Theme"] = theme
                window.close()
                sg.theme(theme)
            settings["Export Pantheon"] = values["--ExportPanth--"]
    settings["Export Pantheon"] = values["--ExportPanth--"] # make sure settings are exported
    window.close()
    return settings

        
    
    
    
