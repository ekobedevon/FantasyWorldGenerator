import Generator
import PySimpleGUI as sg
class NPC():
    race = ""
    name = ""
    sex = ""
    age = 0
    profession = ""
    def __init__(self,gen: Generator.generator = None,dict_data = None, isAdult:bool = True):
        if dict_data == None:
            self.race = gen.generateRace()
            self.sex = Generator.generateGender()
            self.name = gen.generateName(self.race,self.sex)
            self.age = gen.generateAge(self.race,isAdult)
            self.profession = gen.generateProfession()
        else:
            self.name = dict_data['name']
            self.age = dict_data['age']
            self.race  = dict_data['race']
            self.profession = dict_data['profession']
            self.sex =['sex']

    
    def createDisplay(self):
        sg.theme('DarkAmber')    # Keep things interesting for your users

        layout =[[sg.Text('NPC TEXT')],
            [sg.Text(self.name)],
            [sg.Text(self.race)],
            [sg.Text(self.sex)],
            [sg.Text(self.age)],
            [sg.Text(self.profession)]]      

        window = sg.Window('Window that stays open', layout)       
        window.read()
        window.close()
    def createDisplayA(self):
        layout =[[sg.Text('NPC TEXT')],
            [sg.Text("Name: " + self.name)],
            [sg.Text("Race: " +self.race)],
            [sg.Text("Sex: " +self.sex)],
            [sg.Text("Age: " +str(self.age))],
            [sg.Text("Profession: " +self.profession)]]      

        return layout


    
    