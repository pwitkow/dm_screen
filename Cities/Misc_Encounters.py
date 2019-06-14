#extra encounters

import sys, random, os

#base path
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(os.path.join(basepath, 'Scripts'))
import NPCs


import numpy as np

#make some antlions
f=[NPCs.GenMons(8, Class= "Antlion", name="Antlion_A"),
NPCs.GenMons(10, Class= "Antlion", name="Antlion_B"),
NPCs.GenMons(8, Class= "Bandit", name="Bandit_Thievs"),
NPCs.GenMons(20, Class= "Bandit", name="Bandit_B"),
NPCs.GenMons(2, Class= "Basilisk", name="Basilisk_A")]

TotalPop=[]
for sset in f:
    TotalPop.extend(sset)
    

