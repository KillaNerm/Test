import random


class Character:
 
    
    def selectclass(self):
        while True:
            option = input("1 - strenght \n2 - agility \n3 - intelligence \nSelect a class: " )
            if option in ["1", "2", "3"]:
                return int(option)
            else:
                print("Invalid input, try again!")
            
            
    def classstrenght(self, clas):
        if clas == 1:            
            return random.randrange(27, 39)
        else:
            return random.randrange(12, 21)
 
             
    def classagility(self, clas):
        if clas == 2:            
            return random.randrange(27, 39)
        else:
            return random.randrange(12, 21)  
 
                
    def classintelligence(self, clas):
        if clas == 3:            
            return random.randrange(27, 39)
        else:
            return random.randrange(12, 21) 
        
            
    def characterclass(self, clas):
        if clas == 1:
            return "Heavy"

        elif clas == 2:
            return "Assasin"

        elif clas == 3:
            return "Wizard"
     
              
    def __init__(self, name):
        self.name = name
        self.optionclas = self.selectclass()
        self.type = self.characterclass(self.optionclas)
        self.strenght = self.classstrenght(self.optionclas)
        self.agility = self.classagility(self.optionclas)
        self.intelligence = self.classintelligence(self.optionclas)


    def get_stats(self):
        print("Name:", self.name, "\nClass:", self.type, "\nStrenght:", self.strenght, "\nAgility:", self.agility, "\nIntelligence:", self.intelligence)
        
        

class Hero(Character):
    
    
    def selectweapon(self):
        x = input("Select a weapon: ")
        return x

    
    def selectarmor(self):
        x = input("Select a armor: ")
        return x
    
    
    def __init__(self, name):
        super().__init__(name)
        self.weapon = self.selectweapon()
        self.armor =  self.selectarmor()
        
    def get_stats(self):
        super().get_stats()    
        print("Weapon: ", self.weapon, "\nArmor: ", self.armor)
        
        
        
        
        
# maxi = Hero("Cool")
# maxi.get_stats()
# maxvell = Character("Quensi")
# print(maxvell.name)
# maxvell.get_stats()