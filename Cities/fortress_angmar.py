import sys, random, os
import numpy as np
#base path
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(os.path.join(basepath, 'Scripts'))
import Helpers, NPCs 
import Items_New as it

#guy to save
commander_navlen = NPCs.NPC(Level=5, AC=15, Dmg='2d10', Name='Commander Navel')

#Warden, needs a good gun
commander_ardeth = NPCs.NPC(Level=5, Dmg='2d8', Name='Commander Ardeth', AC=20)
ogre = NPCs.monster(Race='Ogre', Name='Orge')

ofs=[NPCs.NPC(Level=2, Dmg='1d4', Name='soldier', AC=12, Stuff=[thing for thing in it.Weapons if thing['Item']=='Spear']) for i in range(200)]

TotalPop=[commander_ardeth, commander_navlen, ogre]
TotalPop.extend(ofs)