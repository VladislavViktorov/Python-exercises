from errors import *
class Character:
    def __init__(self,name,sex, mainwepon,additionalweapon,gameclass) -> None:
        self.name = name
        self.sex = sex
        self.mainweapon = []
        self.additionalweapon = []
        self.gameclass = gameclass
    def print(self):
        return f"User({self.name}, {self.sex}, {self.mainweapon}, {self.additionalweapon},{self.gameclass})"
    
    def add_character(self,name):
        if name not in self.name:
            raise CharacterExists("Error:This character exists")

    def add_weapon(self,weapon):
        if weapon in self.weapon:
            raise InvalidCommand("Error this weapon exists")
