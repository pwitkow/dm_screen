# _____ work camp

'''prison they have to break into'''
import sys, random, os
import numpy as np
#base path
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(os.path.join(basepath, 'Scripts'))
import Helpers, NPCs 
import Items_New as it

#guy to save
clive = NPCs.NPC(Level=4, Dmg='1d4', Name='Clive', Special="Must make it out of the prison alive or else the player can't make the bomb",
                 Stuff=[np.random.choice(it.commonWeapons)])

#Warden, needs a good gun
Warden = NPCs.NPC(Level=8, Dmg='1d6', Name='Warden', AC=17 ,Stuff=[thing for thing in it.Weapons if thing['Item']=='Browning BPS 10-gauge'])

ofs=[NPCs.NPC(Level=5, Dmg='1d4', Name='Officer'+str(i), 
              Stuff=[np.random.choice([u for u in it.commonWeapons if (u["Item"]=='Gloc.' or u["Item"]=='Baton' or u["Item"]=='M16 5.56 Assult Rifle')])]) for i in range(30)]


TotalPop=[clive, Warden]
TotalPop.extend(ofs)
