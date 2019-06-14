#Spare groups for misc battles

import sys, random
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff")
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff\Scripts")
import Helpers, Items, NPCs, Spells
import Int2char
from Helpers import *

Carrions=NPCs.GenMons(10, Class= "Carrion", name="Carrion")

Goblins=NPCs.GenMons(15, Class="Goblin", name="Goblin")
    
Azers=NPCs.GenMons(20, Class="Goblin", name="Goblin")  



TotalPop=[]
TotalPop.extend(one)