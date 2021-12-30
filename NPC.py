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
    background = ""
    goals = ""
    background_details = {}
    def __init__(self,gen: Generator.generator = None,dict_data = None, isAdult:bool = True,goals:str = ""):
        self.background_details = {}
        if dict_data == None:
            self.race = gen.generateRace()
            self.sex = Generator.generateGender()
            self.name = gen.generateName(self.race,self.sex)
            self.age = gen.generateAge(self.race,isAdult)
            self.profession = gen.generateProfession()
            self.background, self.background_details = gen.generateBackground()
            self.goals = goals
        else:
            self.name = dict_data['name']
            self.age = dict_data['age']
            self.race  = dict_data['race']
            self.profession = dict_data['profession']
            self.sex =['sex']

    
   

    def createDisplay(self):
        profession_text = textwrap.wrap("Profession: " + self.profession,30)
   
        layout =[[sg.Text("General Details",font=s.Title_Style)],
            [sg.Text("Name: "+self.name)],
            [sg.Text("Race: " +self.race)],
            [sg.Text("Sex: " +self.sex)],
            [sg.Text("Age: " +str(self.age))]]
        for text in profession_text:
            layout.append([sg.Text(text)])
        layout.append([sg.Text("Personality",font=s.Title_Style)])
        layout.append([sg.Text("Background: "+self.background)])
        for key in self.background_details:
            layout.append([sg.Text(key+": "+self.background_details[key])])
        if self.goals != "":
            layout.append([sg.Text("Personal Goal",font=s.Title_Style)])
        
        layout = [[sg.Frame("NPC: " + self.name,layout)]]

        return layout


    
    