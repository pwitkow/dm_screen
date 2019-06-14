import sys
import os
base_path=os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.append(base_path)
sys.path.append(os.path.join(base_path, 'Scripts'))
sys.path.append(os.path.join(base_path, 'Cities'))
import Items_New
from Tkinter import *
from Helpers import *
import RandomEn
from PIL import Image, ImageTk
import importlib
import pickle
import ttk

width=1200
length=650

global char
global data
root=Tk()

root.geometry(str(width)+'x'+str(length)+"+200+200")
root.title("DM's Window")
nb=ttk.Notebook()

#image = Image.open("C:\Users\Phillip\Desktop\Dnd Stuff\Images\Parchment.jpg").resize((width,length))
#background_image=ImageTk.PhotoImage(image)
#background_label = Label(root, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

'''Main window for DM'''
App= ttk.Frame(nb)
nb.add(App, text='Main')

div_long=Canvas(App, width = 5, height = length, bg = "black")
div_height=Canvas(App, width = 742, height = 5, bg = "black")
div_long.place(x=745,y=0)

div_height.place(x=0,y=330)

cityPath=os.path.join(base_path, 'Cities')

StoryPath=os.path.join(base_path, 'Stories')





#save button is always good

def sav():
    name=city.get() if '.dat' in city.get() else city.get()+'.dat'
    with open(os.path.join(cityPath,name), 'wb') as flo:
        pickle.dump(data, flo, protocol=2)
savButton=Button(App, text="Save", command=sav)
savButton.grid(column=5, row=0)




'''make a way to change cities'''
#label and city entry
city_box=Label(App, text="Current City")
city_box.grid(column=0, row=0)
city=Entry(App)
city.insert(END, "Ukriah")
city.grid(column=0,row=1)

#distance entry for radnome encounters
dis_label=Label(App, text="Distance")
dis_label.grid(column=1, row=0)
dis=Entry(App)
dis.insert(END, 10)
dis.grid(column=1, row=1)
#go button




#make a main list box for the general populace
list_box_label=Label(App, text="Populace")
list_box_label.grid(column= 0, row=2)
list_box= Listbox(App, selectmode="BROWSE",height=16)
list_box.grid(column= 0, row=3, rowspan=8, sticky=N)
#scrollbar.pack(side="right", fill="y")

"""Widgets for characgter display------------------------------------------------"""

#Name and HP
name_label=Label(App, text="Name")
name_label.grid(column= 1, row=2)
name=Entry(App)
name.grid(column=1, row=3, sticky=N)

#HP display and change button
healthButton=Label(App, text='Health')
healthButton.grid(column=2, row=2) 
health=Entry(App)
health.grid(column=2, row=3, sticky=N)


level_label=Label(App, text="Level")
level_label.grid(column= 4, row=2)
lev=Entry(App)
lev.grid(column=4, row=3, sticky=N)

race_label=Label(App, text="Race/Type")
race_label.grid(column=5, row=2)
race=Entry(App)
race.grid(column=5, row=3, sticky=N)

#makes a list bow for all the stats
stats_Label=Label(App, text="Character stats")
stats_Label.grid(column=1, row=4, sticky=N)
stats_box=Listbox(App, selectmode="BROWSE", height=10)
stats_box.grid(column=1, row=5, rowspan=4)

#Spells 
spells_label=Label(App, text='Spells')
spells_label.grid(column=2, row=4)
spells_box=Listbox(App, selectmode="Browse", height=10)
spells_box.grid(column=2, row=5,rowspan=4)

def findSpell():
    SpellHelp(spellHelp_box.get())
spell_help=Button(App, text='Spell Help', command=findSpell)
spell_help.grid(column=1, row=9)
spellHelp_box=Entry(App)
spellHelp_box.grid(column=1, row=10)

#items boxes
items_label=Label(App, text="Gear")
items_label.grid(column=3, row=4)
items_box=Listbox(App, selectmode="BROWSE", height=10)
items_box.grid(column=3, row=5,rowspan=4)

#Special abilites/questsbox
special_label=Label(App, text="Special")
special_label.grid(column=4, row=4)
special_box=Text(App, height=10, width=30)
special_box.grid(column=4, row=5, columnspan=3, rowspan=4, sticky=W)


#gold stuff
gold_label=Label(App, text="Gold")
gold_label.grid(column= 3, row=2)
gold=Entry(App)
gold.grid(column=3, row=3, sticky=N)

def findName(name, list):
    for i in list:
        if i.getStats()["Name"]==name:
            return i
    
    
def enterStats(box, dicti, item="Stats", replace=True):
    #this function enters the stuff for characters into each window
    holder=dicti.getStats()
    if item=="Special":
        box.delete('1.0',END)
    else:
        if replace==True:
            box.delete(0, END)
    if isinstance(holder[item], dict): 
        for key in sorted(holder[item].keys()):
            box.insert(END, (str(key) + " : " + str(holder[item][key])))
    elif isinstance(holder[item], list):
        if not holder[item]:
            pass
        else:
            if isinstance(holder[item][0] , dict):
                for obj in holder[item]:
                    box.insert(END, obj['Item'] + ' : ' + str(obj['Price']) + 'gp : ' + str(obj['Stats']))
            else:
                for obj in holder[item]:
                    box.insert(END, str(obj))
    else:
        box.insert(END, str(holder[item]))


def saveStats(yy):
    if gold.get()!='':
        yy.setGold(float(gold.get()))
    yy.setHP(int(health.get()))
    yy.setSpecial(special_box.get('1.0',END))    

#updates all of the stats and what not for the character entries  
def up_date(event):
    try:
        saveStats(char)
    except NameError:
        pass
    else:
        saveStats(char) 
    spells_box.delete(0,END) 
    
    char=findName(list_box.get(list_box.curselection()), data)
    enterStats(stats_box, char)
    enterStats(health, char, item="HP")
    enterStats(gold, char, item="Gold")
    enterStats(lev, char, item="Level")
    enterStats(race, char, item="Race")
    enterStats(items_box, char, item="Stuff")
    if char.__class__.__name__=='warrior':
        enterStats(items_box, char, item="Gear", replace=False)
        enterStats(spells_box, char, item="Spells")
    elif char.__class__.__name__=='merchant':
        enterStats(items_box, char, item="Goods")
    if char.__class__.__name__=="monster":
        gold.delete(0,END)
    
    enterStats(special_box, char, item="Special")
    #udates window when click happens 
    name.delete(0, END)
    name.insert(END, list_box.get(list_box.curselection()) )    
    App.update()  

list_box.bind('<<ListboxSelect>>', up_date)


#widget for xp counting
sessionXp=XpCounter(0)
def set_XP():
    if int(char.getStats()["HP"])<1:
        sessionXp.addXP(int(char.getExp()))
        xp_track.delete(0, END)
        xp_track.insert(END, str(sessionXp.getXP()))
    else:
        sessionXp.addXP(int(xp_track.get()))
        xp_track.delete(0, END)
        xp_track.insert(END, str(sessionXp.getXP()))        
xp_button=Button(App, text="Add XP", command=set_XP)
xp_button.grid(column=4, row=0, sticky=N)
xp_track=Entry(App)
xp_track.grid(column=4, row=1)


def newCity():
    #function for loading new city
    if city.get()=='RandomEncounter':
        '''UNDER CONSTRUCTION'''
        #deals with random encounters/ resets dis to left over miles 
        global data
        data=RandomEn.randEncounter(int(dis.get()))
        dis.delete(0,END)
        dis.insert(END, data[1])
        data=data[0]
    #temporary fix so that i can load saved files and new modules until everything works in window)    
    elif city.get()[-4:]=='.dat':
        with open(os.path.join(cityPath,city.get()), 'rb') as fl:
            data=list(pickle.load(fl))
    else:    
        module=importlib.import_module(city.get())
        
        data=module.TotalPop
    
    list_box.delete(0, END)
    for item in data:
        list_box.insert(END, item.getStats()["Name"])

city_button=Button(App, text='GO', command=newCity)
city_button.grid(column=2, row=0)  

#Dm's Notes Section___________________________________________________
notes_Label=Label(App, text="DM\'s Story Notes")
notes_Label.place(x=755, y=0)
note_book=Notes()
camp_Title=Entry(App)
camp_Title.place(x=860, y=0)
def sav_Notes():
    #for saving stories
    note_book.updateText(note_pad.get('1.0',END))
    name=camp_Title.get() if '.dat' in camp_Title.get() else camp_Title.get()+'.dat'
    with open(os.path.join(StoryPath,name), 'wb') as St:
        pickle.dump(note_book, St, protocol=2)   
note_Save=Button(App, text="Save", command=sav_Notes)
note_Save.place(x=1000,y=0)

def loadNotes():
    name=camp_Title.get() if '.dat' in camp_Title.get() else camp_Title.get()+'.dat'
    with open(os.path.join(StoryPath, name), 'rb') as St:  
        global note_book
        note_book=pickle.load(St)
        note_pad.delete('1.0', END)
        note_pad.insert(END, note_book.get_Text())

#load button
load_button=Button(App, text='Load', command=loadNotes)
load_button.place(x=1100, y=0)
#pad for texts
     #add scrollbar

#figure out the scroll thing
note_pad=Text(App, height=30, width=52, wrap=WORD)
note_pad.place(x=755, y=30)


#dice rollers!

d_four=dice_roller(App, num=4)
d_four.put_it((30,380), spread=70)

d_six=dice_roller(App, num=6)
d_six.put_it((30,420), spread=70)

d_eight=dice_roller(App,num=8)
d_eight.put_it((30,460), spread=70)

d_ten=dice_roller(App,num=10)
d_ten.put_it((30,500), spread=70)

d_twelve=dice_roller(App,num=12)
d_twelve.put_it((30,540), spread=70)

d_twenty=dice_roller(App,num=20)
d_twenty.put_it((30,580), spread=70)










'''City creator tab'''
CC_tab= ttk.Frame(nb)
nb.add(CC_tab, text='City Creator')
div_height=Canvas(App, width = width, height = 5, bg = "black")
char_list=[]

'''make a way to change cities'''
#label and city entry
cc_city_box=Label(CC_tab, text="City Name")
cc_city_box.grid(column=0, row=0)
cc_city=Entry(CC_tab)
cc_city.insert(END, "New City")
cc_city.grid(column=0,row=1)

NPC_num_choice=Entry(CC_tab)
NPC_num_choice.place(x=100, y=300)



NPC_choices={'General NPC':["None"], 'Merchant':["General","Weps", "Armor"
                                              "Blksmith"]}

class_name=StringVar(CC_tab)
class_name.set("Class Type")

def uptypes(x,y,z):
    new_choices = NPC_choices[NPCty_choice.get()]
    class_select['menu'].delete(0, 'end')
    for ch in new_choices:
            class_select['menu'].add_command(label=ch)#, command=class_name.set(ch))    
       

class_select=OptionMenu(CC_tab, class_name, *NPC_choices["General NPC"])
class_select.place(x=250, y=350)

NPCty_choice = StringVar(CC_tab)
NPCty_choice.trace('w', uptypes)
NPCty_choice.set("General NPC")

NPC_type=OptionMenu(CC_tab, NPCty_choice, *NPC_choices.keys())
NPC_type.place(x=10, y=350)



def gen_chars():
    add_NPCs=[NPCs.NPC(level=int(NPC_level_choice.get())) for num in range(int(NPC_num_choice.get()))]
    char_list.extend(add_NPCs)
    
    #think of a faster way to add characters
    cc_NPCs_Box.delete(0, END)
    for item in add_NPCs:
        cc_NPCs_Box.insert(END, item.getStats()["Name"])    

#City Character list
cc_NPCs_gen=Button(CC_tab, text="Generate", command=gen_chars)
cc_NPCs_gen.place(x=150,y=50)
cc_NPCs_Box=Listbox(CC_tab, selectmode="BROWSE", height=12, width=33) 
cc_NPCs_Box.place(x=10, y=100)










'''Items/Tresure Tab'''
Tres_tab= ttk.Frame(nb)
nb.add(Tres_tab, text='Tresure Tab')
def item_finder():
    if itChoice.get().lower().replace(' ','') in Items_New.Total_Cats:
        itms=[item for item in Items_New.items if itChoice.get().lower().replace(' ', '') in item['Type'].lower().replace(' ', '')]
    else:
        itms=[item for item in Items_New.items if itChoice.get().lower().replace(' ', '') in item['Item'].lower().replace(' ', '')]
    it_search_Box.delete(0,END)
    for it in itms:
        it_search_Box.insert(END,[str(key) + ' : ' + str(it[key]) for key in it.keys()] )
    Tres_tab.update()

#1200x600
it_search=Button(Tres_tab, text="Item Search", command=item_finder)
it_search.place(x=540,y=370)
it_search_Box=Listbox(Tres_tab, selectmode="BROWSE", height=12, width=33) 
it_search_Box.place(x=540, y=400)


itChoice=Entry(Tres_tab)
itChoice.place(x=615, y=375)
#itHelp=Entry(App)
#itHelp.grid(column=3, row=10)

# make stuff to generate chyest loot
choices=['Caravan', 'Military Chest', 'Supply','Commerce','Treasure','Magic Chest']
variable = StringVar(App)
variable.set("Type")
chest_type=OptionMenu(Tres_tab, variable, *choices)
chest_type.place(x=10, y=350)

# number entry
num_choice=Entry(Tres_tab)
num_choice.place(x=90, y=350, width=50, height=20)

lev_choice=Entry(Tres_tab)
lev_choice.place(x=250, y=350, width=50, height=20)

def gen_Tres():
    global Tresure_Chests
    Tresure_Chests=[Items_New.chest(level=int(lev_choice.get()), 
                          Name=variable.get()+'_'+ str(num),        
                    Typer=variable.get()) for num in range(int(num_choice.get()))]
    for box in Tresure_Chests:               
        tres_Box.insert(END, box.getName())        

#Treasure box
tres_gen=Button(Tres_tab, text="Generate", command=gen_Tres)
tres_gen.place(x=150,y=350)
tres_Box=Listbox(Tres_tab, selectmode="BROWSE", height=12, width=33) 
tres_Box.place(x=10, y=400)

contents_Box=Listbox(Tres_tab, selectmode="BROWSE", height=12, width=33) 
contents_Box.place(x=300, y=400)

def look_tres(event):
    #find the chest with the matching name
    Tres_chest=[c_box for c_box in Tresure_Chests if c_box.getName()==tres_Box.get(tres_Box.curselection())][0]
    contents_Box.delete(0,END)
    for item in Tres_chest.getTres():
        contents_Box.insert(END, 'Item : '+ item['Item']+','+'Value : '+str(item['Price']))
    #udates window when click happens   
    Tres_tab.update()  

tres_Box.bind('<<ListboxSelect>>', look_tres)




nb.pack(expand=1, fill="both")

root.mainloop()

#App.mainloop()




