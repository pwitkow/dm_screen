#Red Valley
import sys, random, os
import numpy as np
#base path
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(os.path.join(basepath, 'Scripts'))
import Helpers, NPCs 
import Items_New as it

#gun smiths
guns=[NPCs.merchant(Type="Weps", Str=3, Gold=random.randint(20, 300)) for i in range(6)]
for l in guns:
    l.name=l.name+' Guns'

#armorers
armr=[NPCs.merchant(Type="Armor", Str=3, Gold=random.randint(20, 300)) for i in range(6)]
for ar in armr:
    ar.name=ar.name+' Armor'
    
#fences
fences=[NPCs.merchant(Type="Thief", Str=3, Gold=random.randint(50, 200)) for i in range(6)]
for gh in fences:
    gh.name=gh.name+' Fence'


#in keepers
ct=NPCs.merchant(Name="Clayton (BT: Dirty Dan's", Type="InnKeep", Gold=350)
dt=NPCs.merchant(Name='Eugene (BT: The Dirt Pounder)', Type="InnKeep", Gold=350)
et=NPCs.merchant(Name='Durstin (BT: The High Quarter)', Type="InnKeep", Gold=350)
ft=NPCs.merchant(Name='Jerry (BT: Sandy Dunes)', Type="InnKeep", Gold=350)


genpop=NPCs.GenNPCs(100)

TotalPop=[]
TotalPop.extend(guns)
TotalPop.extend(armr)
TotalPop.extend(fences)
TotalPop.extend(genpop)
TotalPop.append(ct)
TotalPop.append(dt)
TotalPop.append(et)
TotalPop.append(ft)

print TotalPop