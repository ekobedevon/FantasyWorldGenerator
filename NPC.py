import textwrap
import Generator
import Style as s
import PySimpleGUI as sg
class NPC():
    race = ""
    name = ""
    sex = ""
    age = 0
    profession = ""
    origin = ""
    goals = ""
    lair = ""
    origin_details = {}
    def __init__(self,gen: Generator.generator = None,dict_data = None, isAdult:bool = True,goals:str = ""):
        self.origin_details = {}
        if dict_data == None:
            self.race = gen.generateRace()
            self.sex = Generator.generateGender()
            self.name = gen.generateName(self.race,self.sex)
            self.age = gen.generateAge(self.race,isAdult)
            self.profession = gen.generateProfession()
            self.origin, self.origin_details = gen.generateOrigin()
            self.goals = goals
        else:
            self.name = dict_data['name']
            self.age = dict_data['age']
            self.race  = dict_data['race']
            self.profession = dict_data['profession']
            self.sex =['sex']

    
   

    def createDisplay(self):
   
        layout =[[sg.Text("General Details",font=s.Title_Style)],
            [sg.Text("Name: "+self.name)],
            [sg.Text("Race: " +self.race)],
            [sg.Text("Sex: " +self.sex)],
            [sg.Text("Age: " +str(self.age))],
            [sg.Text("Lair: " +self.lair)]]
        layout.append([sg.Text("Profession:" + self.profession)])
        layout.append([sg.Text("Personality",font=s.Title_Style)])
        layout.append([sg.Text("Origin: "+self.origin)])
        for key in self.origin_details:
            layout.append([sg.Text(key+": "+self.origin_details[key])])
        if self.goals != "":
            layout.append([sg.Text("Goal",font=s.Title_Style)])
            layout.append([sg.Text(self.goals,font=s.Text_Style)])
        
        layout = [[sg.Frame("NPC: " + self.name,layout)]]

        return layout


    
    