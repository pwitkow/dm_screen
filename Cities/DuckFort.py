'''prison they have to break into'''
import sys, random, os
import numpy as np
#base path
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(os.path.join(basepath, 'Scripts'))
import Helpers, NPCs 
import Items_New as it

#guy to save
iona = NPCs.NPC(Level=10, AC=22, Dmg='2d10', Name='Iona', Special="Has the rest of the Duck Tails Book",
                 Stuff=[thing for thing in it.Weapons if thing['Item']=='Browning BPS 10-gauge'])

#Warden, needs a good gun
Derik = NPCs.NPC(Level=8, Dmg='2d8', Name='Deric', AC=20)

ofs=[NPCs.NPC(Level=5, Dmg='1d4', Name='Officer'+str(i), AC=18,
              Stuff=[np.random.choice([u for u in it.commonWeapons if (u["Item"]=='Gloc.' or u["Item"]=='Baton' or u["Item"]=='M16 5.56 Assult Rifle')])]) for i in range(16)]


TotalPop=[iona, Derik]
TotalPop.extend(ofs)