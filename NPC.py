import textwrap
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
        profession_text = textwrap.wrap("Profession: " + self.profession,30)
        layout =[[sg.Text('NPC TEXT')],
            [sg.Text("Name: " + self.name)],
            [sg.Text("Race: " +self.race)],
            [sg.Text("Sex: " +self.sex)],
            [sg.Text("Age: " +str(self.age))]]
        for text in profession_text:
            layout.append([sg.Text(text)])
             

        return layout


    
    