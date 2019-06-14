#Dirty Dans Water Hole 
import sys, random, os
import numpy as np
#base path
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(os.path.join(basepath, 'Scripts'))
import Helpers, NPCs 
import Items_New as it

#bartender
bt=NPCs.merchant(Name='Clayton (Bartender)', Type="InnKeep", Gold=350)

#drunks
dr=NPCs.GenNPCs(4, Lev=1)

#gangMembers
gms=[NPCs.NPC(Level=5, Dmg='1d4', Name='Silver Tooth'+str(i) ,Stuff=[np.random.choice(it.commonWeapons)]) for i in range(3)]

#officers
ofs=[NPCs.NPC(Level=5, Dmg='1d4', Name='Officer'+str(i), Stuff=[u for u in it.commonWeapons if u["Item"]=='Gloc.' or u["Item"]=='Baton']) for i in range(3)]



TotalPop=[]
TotalPop.extend(dr)
TotalPop.extend(gms)
TotalPop.extend(ofs)
TotalPop.append(bt)

