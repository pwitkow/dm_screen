import os, sys,csv
from ast import *
from math import *
from collections import *
import random
base_path=os.path.normpath(os.getcwd() + os.sep + os.pardir)
os.chdir(os.path.join(base_path, 'Items'))
path=os.path.join(base_path, 'Items')

file=csv.DictReader((open(os.path.join(path,'Master.csv'), 'r+')))
def Order_List(x):
    order=['Item','Price','Stats','Type','Weight','Special']
    return [(i,x[i]) for i in order]

items=[]
for dics in file:
    dics['Stats']=literal_eval(dics['Stats'])
    dics["Price"]=float(dics["Price"].replace(",",''))
    items.append((OrderedDict((Order_List(dics)))))

GeneralGoods=[thing for thing in items if thing['Type']=="Trade Good"]
Junk=[thing for thing in items if thing['Type']=="Junk"]
AdvGear=[thing for thing in items if thing['Type']=="Adventuring Gear"]
Food=[thing for thing in items if thing['Type']=="Food"]
Taboo=[thing for thing in items if thing['Type']=="Taboo"]
Weapons=[thing for thing in items if thing['Type']=="Weapon"]
Armor=[thing for thing in items if thing['Type']=="Armor"]
Rooms=[thing for thing in items if thing['Type']=="Room"]
Gemstone=[thing for thing in items if thing['Type']=="Gemstone"]
Art=[thing for thing in items if thing['Type']=="Art Object"]


#Common Weapons/Armor
commonWeapons=["Dagger", "Gloc.", "Handaxe","Shiv", "Baton", "AK-47 7.62x39mm"]
commonWeapons=[Wep for Wep in Weapons if Wep['Item'] in commonWeapons]
LightArmor=[Amr for Amr in Armor if Amr['Item']=='Leather Jacket' or Amr['Item']=='Hickey Pads']*15

Total_Cats=list(set([dic['Type'].lower().replace(' ','') for dic in items]))


#class for chests
class chest:
    def __init__(self, level=None, Typer=None, Name=None):
        self.name = Name
        self.level=1 if level==None else level
        self.DC=int(log((self.level**2), 2))
        self.gold=((self.level/2.0)+1)**4 if Typer.lower().replace(" ","")=="magicchest" else round((round(random.random(),1)*(((self.level/2.0)+1)**3)))
        self.Type="caravan" if Typer==None else Typer
        
        #generate treasures
        def genTreasure(gold, Type):
            gegs=gold
            gg=gegs*.9 if Type.lower().replace(" ","")=="magicchest" else round((gegs * random.random()),2) 
            tres=[]
            if Type.lower().replace(" ","")=='caravan': #carvan (contains anything)
                itms=[thing for thing in items if float(thing['Price']) < gg]
                if random.randint(1,100) in range(37,42) and Taboo:
                    itms[0:0] = Taboo                
            elif Type.lower().replace(" ","")=="militarychest": #military chest (armor/weps)
                itms=[thing for thing in Weapons+Armor if float(thing['Price']) <gg ]
            elif Type.lower().replace(" ","")=='supply': #supply (trade goods/food/junk)
                itms=[thing for thing in GeneralGoods+Food+Junk if float(thing['Price']) <gg ]
                if random.randint(1,100) in range(37,42) and Taboo:
                    itms[0:0] = Taboo
            elif Type.lower().replace(" ","")=='commerce':#commerce(adventuring gear/food/junkW)
                itms=[thing for thing in AdvGear+Food+Junk if float(thing['Price'])<gg]
                if random.randint(1,100) in range(37,42) and Taboo:
                    itms[0:0] = Taboo                
            elif Type.lower().replace(' ','')=='magicchest':
                itms=[thing for thing in Magic if float(thing['Price'])<gg]
            elif Type.lower().replace(' ','')=='tresurechest':
                itms=[thing for thing in Art+Gemstones if float(thing['Price'])<gg]
            else:
                return "Not a Valid Entry"
            if itms:
                while gegs > gg:
                    holder=random.choice(itms)
                    if gegs-holder["Price"]<0:
                        break
                    else:
                        gegs=gegs-holder["Price"]
                        tres.append(holder)
            return tres, round(gegs,2)
        
        hold=genTreasure(self.gold, Type=self.Type)
        self.Treasure=hold[0]
        self.gold=hold[1]
    
    def getTres(self):
        return self.Treasure
    
    def getGold(self):
        return self.gold
    
    def addTres(self, itmen):
        self.Treasure[0:0]=[t for t in items if t['Item']==item]
        return self.Treasure
    
    def getName(self):
        return self.name
        