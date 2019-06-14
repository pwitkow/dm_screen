#random encounters map
import sys, random
import os
base_path=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(base_path)

import NPCs
import Helpers, Items, NPCs
from Helpers import *

commonHunters=["Boar", "Black Bear","Wolf"]
commonHunted=["Badger","Deer","Elk"]

commonHumans=["Bandit","Thug"]

def randEncounter(miles):

    for i in range(miles):
        en=random.randint(1,100)
        #Enconter is a battle 
        if en in range(91,95):
            ll=random.choice(commonHunters)
            return NPCs.GenMons(random.randint(2,5), Class=ll),i
        #encounter is hunting opprotunity
        elif en in range(25,35):
            ll=random.choice(commonHunted)
            return NPCs.GenMons(random.randint(1,3), Class=ll),i



    