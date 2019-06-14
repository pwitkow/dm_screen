import sys, random
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff\Scripts")
import Helpers, NPCs, Spells
import Int2char

#City Folks
BlackSmith=NPCs.merchant(Name="Bur (Black Smith)", Type="BlkSmith", Str=70, Gold=50, Special=" ") 

WeaponSmith=NPCs.merchant(Name="Brihelm (Weapon Smith)", Type="Weps", Str=3, Gold=100, 
                          Special="Quest: Gave his daugther (Erwyn) to young Niwald (oldes son"+ 
                          "of the Bondar family in Rieswald (town) in order to forge a new trading"+
                          "relations with the merchant family. However, their marriage was about 1 month"
                          "ago and he has yet to recieve any good from the family. Go to Reiwald in the north east"+
                          "and remind them of the promises they made during marriage") 

GeneralStore=NPCs.merchant(Name="Garbri (General Goods)", Type="General", Gold = 150, Special='Will give 7sp for finely skinned deer pelts'+
                           'because of the shortage good skinners this winter')

Grimfast=NPCs.warrior(Name="Grimfast", Type="Barbarian", Str=4, Con=3, Int=-2, Dex=4,
                      Weapon="Greataxe", Armor='Studded Leather Armor', Level=10, 
                      Special="Stands outside longhouses and doesnt let the characters in; Leads the Clan senate along "+
                      "with the head Druids; Ultimately makes the decision that no-one will be allowed to travel to the mountian.",
                      Stuff=['Longsword'])

Grimfast=NPCs.warrior(Name="Iseult", Type="Druid", Str=1, Con=4, Int=4,Wis=4, Dex=3,
                      Weapon="Quarterstaff", Armor='Padded Armor', Level=15, 
                      Special="Leader of the druid congregation in Ukriah, asked the the group to wait for 10 days for the scouting party to\
                       but they never did",
                      Stuff=['Longsword'])

BentMuleKeeper=NPCs.merchant(Name='Duren (Bent Mule Keep)', Type="InnKeep", Gold=50)

Seypha=NPCs.warrior(Name='Seypha', Type='Druid', Level=15, Special= "Will teach the group about arcane knowledge and the planes if the bring back the horns of fallen elk stag", Armor=None)

Berenger=NPCs.NPC(Name='Berenger', Race="Half-ling", Special= "Has Duren's Gold, but doesn't want to give it back, his heart was broken by the"+
                  "bar whench and duren treated him bad", Gold=35)
PassedOutWenchKeeper=NPCs.merchant(Name='Kef (POW Keep)', Type="InnKeep", Gold=15, Special="Quite a Bad drinking problem; has"+
                              "accountant (Berenger) who ran off some money, if you find him and get it back Kef promises"+
                              "to give you one of the farm prositutes. She will hava at least 3 teeth.; only discription is;"+
                              "that he is short")
Wizard=NPCs.warrior(Name="Yuesef", Type='Wizard', Level=15)

#GeneralPopulace
GenPop=NPCs.GenNPCs(100, Lev=1)
for r in range(12):
    GenPop.append(NPCs.NPC(Level=2, Special="Looks a little slutish:Will try to pickpocket who ever she talks too first; "+ "If they catch her and roll a DC 14 intimidate or persuasion, she'll tell them about the gambling ring under The Snow Drift Market. Password: UtterBomb"))
    
random.shuffle(GenPop)
GenPop.append(NPCs.NPC(Name="Berenger", Level=3, Gold=100, Special='Kef the bar keep is looking after him; but he owes backwages'+
                       "for about 2 months. So he ran off with about 300gp that he had siphoned from Kefs books; DC check > 16 to"+
                       "persuade him to give it back; Otherwise, itimidate >15"))
GenPop.append(NPCs.NPC(Name="Finneus", Level=5, Str=6, Special="Maiden Gailor has a puppy but da puppy seems to have gone runnin"+
                       "around and got itself a noice cut or two through the leg. I think it might be infected but Maiden Gailor"+
                       "and everyone else haven't given it a notice. I think cutting off the leg will do the trick. Here's some"+
                       "ether and lit'l saw i got to do the job. I'm i bit to big to be snbaeking around lik this, but im sure" +
                       "Maiden Gailor would find it a delightful suprise. Would you go and chop off the puppies leg so that it dont"+
                       "die. I'd hate to see it pass. Maiden Gailor would be IN-CON-SOL-ABLE."))

TotalPop=[BlackSmith,Wizard,Seypha,Berenger, WeaponSmith, GeneralStore, Grimfast, BentMuleKeeper, PassedOutWenchKeeper]
TotalPop.extend(GenPop)