import sys, math, os, random, re
import csv
base_path=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(base_path)
sys.path.append(os.path.join(base_path, 'Scripts'))
import Helpers, Items_New


#List of fantasy names
NameList=[]
Namer=open(os.path.join(base_path, "NPC Stuff\\Modern_Names.csv"), 'r+')
for li in Namer:
    li=re.sub(',,,\\n', '', li)
    NameList.append(str(li))
    
    
    


class NPC: 
    def __init__(self, Name=None, Race=None, AC=None, HP=None, Attack=None, 
                Exp=None,Dmg=None, Level=None, HitDie=None, Gold=None, Str=None,
                Dex=None, Int=None, Wis=None, Cha=None, Con=None, 
                Special=None, Init=None, Stuff=[]):
        
        self.name=random.choice(NameList) if Name == None else Name
        self.level=5 if Level == None else Level
        self.ac= 10 if AC == None else AC
        self.hp= 15 if HP == None else HP 
        self.attack=0 if Attack == None else Attack
        #rounds gold to two sig figs for copper
        self.exp=round(random.randint(100,250)*(self.level),2) if Exp == None else Exp
        self.dmg='1d4' if Dmg == None else Dmg
        self.hitdie= 6 if HitDie== None else HitDie
        self.gold = round((round(random.random(),2)*((self.level/2.0)**3))) if Gold == None else Gold 
        #Default attirbutes are randomly assigned such that -3<x<3
        self.Str= random.randint(-2,3) if Str == None else Str
        self.Dex= random.randint(-2,3) if Dex == None else Dex
        self.Int= random.randint(-2,3)  if Int == None else Int
        self.Cha= random.randint(-2,3)  if Cha == None else Cha
        self.Con= random.randint(-2,3)  if Con == None else Con
        self.Wis= random.randint(-2,3)  if Wis == None else Wis
        self.special=" " if Special == None else Special
        self.race="Human" if Race==None else Race
        self.stuff= [] if Stuff == None else Stuff
        self.Init = self.Dex if Init== None else Init + self.Dex 
        #indicates whether the class is dead
        
    #level up character
        for i in range(self.level):
            self.hp= self.hp + random.randint(1, self.hitdie) 
        self.gold=self.gold*self.level*1.5
        #assign extra stat bonus at random if level
        for i in range((self.level)):
                self.attack+=1
                holder=random.randint(1,6)
                if holder==1:
                    self.Str+=1
                elif holder==2:
                    self.Dex+=1
                elif holder==3:
                    self.Con+=1 
                elif holder==4:
                    self.Int+=1
                elif holder==5:
                    self.Wis+=1
                elif holder==6:
                    self.Cha+=1
    
        for i in range(random.randint(0,2)):
            self.stuff.append(random.choice(Items_New.GeneralGoods)) #change back to junk
        #1 in 75 chance of having a "Taboo Good"
        if random.randint(1,75)==12:
            self.stuff.append(random.choice(Items_New.Taboo))
        #1 in 40 chance of having good item set
        if random.randint(1,40)==12:
            self.stuff.append(random.choice(Items_New.GeneralGoods))            
       
        self.attack=self.attack + self.Str
    
    def getExp(self):
        return self.exp
    
    def getDmg(self):
        return self.dmg 
    
    def setHP(self, amount):
        self.hp= amount
        return self.hp
    
    def setSpecial(self, spec):
        self.special=spec
        return spec
   
    
    def getStats(self):
        pers={"Name": self.name,"Race": self.race, "Level" : self.level, "HP": self.hp, "Stuff": self.stuff, "Gold":self.gold,
        "Special": self.special, "Stats":{"Str":self.Str, "Dex" :self.Dex,"Con": self.Con, "Int: ":self.Int, "Wis": self.Wis, "Cha":self.Cha,
          "Attack Bonus":self.attack, "Attack Dmg": self.dmg, "Attack Init":self.Init, "AC":self.ac }}
        return pers 
   
    def setGold(self, amount):
        self.gold=amount 
        return self.gold



class merchant(NPC):
    def __init__(self,Goods=[],
                 Type=None, *args,**kwargs):
        #intinitalize base class and pass any agruments from child
        NPC.__init__(self, *args, **kwargs)
        
        #populate the merchants 'inventory' with appropriate items
        self.Type="General" if Type == None else Type
        self.goods= [] if Goods == [] else Goods
        #add the rest of the things to stuff
        if self.Type=="General":
            for i in range(1,random.randint(10,30)):
                self.goods.append(random.choice(Items_New.GeneralGoods))
        elif self.Type == "Weps":
            for i in range(1,random.randint(10,30)):
                self.goods.append(random.choice(Items_New.Weapons))
        
        elif self.Type == "Armor":
            for i in range(1,random.randint(10,30)):
                self.goods.append(random.choice(Items_New.Armor))                 
        
        elif self.Type == "InnKeep":
            self.goods = Items_New.Food + Items_New.Rooms
            
        elif self.Type == 'Theif':
            for i in range(1,random.randint(4,10)):
                self.goods.append(random.choice(Items_New.Taboo))
            #add general discouted stolen goods to mix
            for i in range(1,random.randint(4,10)):
                self.goods.append(random.choice(Items_New.GeneralGoods))       
            for i in range(1,random.randint(2,3)):
                self.goods.append(random.choice(Items_New.Gemstone)) 

        
    def getStats(self):
        pers={"Name": self.name,"Race": self.race, "Level" : self.level, "HP": self.hp, "Stuff": self.stuff, "Gold":self.gold,
        "Special": self.special, "Stats":{"Str":self.Str, "Dex" :self.Dex,"Con": self.Con, "Int: ":self.Int, "Wis": self.Wis, "Cha":self.Cha,
          "Attack Bonus":self.attack, "Attack Dmg": self.dmg, "Attack Init":self.Init, "AC":self.ac }, "Goods":self.goods}
        return pers
    


'''Monsters'''    
from ast import literal_eval as make_tuple
path=os.path.join(base_path, 'NPC Stuff\\')
mon=csv.DictReader(open(path+"Monsters.csv","r+"))
monsters=[]
for line in mon:
    monsters.append(line)

class monster(NPC):
    def __init__(self, Race=None, *args, **kwargs):
        if Race==None:
            return "Monster must be Named"
        else:
            self.Race=Race
        mster= next((l for l in monsters if l['Name'] == str(self.Race)), None)
        
        NPC.__init__(self,Race=self.Race,AC=int(mster['AC']), HP=int(mster["HP"]), 
                Exp=mster['XP'],Dmg=mster["Dmg"], HitDie=int(mster["HitDie"]),
                Gold=None, Str=int(mster["STR"]),
                Dex=int(mster["DEX"]), Int=int(mster['INT']), Wis=int(mster['WIS']), 
                Cha=int(mster['CHA']), Con=int(mster['CON']), 
                Special=mster['Special'], 
                *args, **kwargs)


def GenNPCs(Number, Lev=1, Class=None,):
    #Generates list of n enemy combatants of a certain Levet
    Ns=[]
    for n in range(Number):
        Ns.append(NPC(Level=Lev))
                    
    return Ns



def GenMons(Number, Class, Level=1, name='a'):
    Mons=[]
    for i in range(Number):
        Mons.append(monster(Race=Class, Name=name+str(i)))
    
    return Mons

