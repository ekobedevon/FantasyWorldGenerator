class NPC():
    def __init__(self, name="",age=-1,race = "npc",profession="npc",dict_data = None):
        if dict_data == None:
            self.name = name
            self.age = age
            self.race  = race
            self.profession = profession

    def NPC2Dict(self):
        export = {'name':self.name,'age': self.age,'race':self.race,'profession':self.profession,}
        return export


    def dict2NPC(self,dict_data):
        self.name = dict_data['name']
        self.age = dict_data['age']
        self.race  = dict_data['race']
        self.profession = dict_data['profession']
        