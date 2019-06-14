import sys
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff")
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff\Scripts")
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff\Cities")
import Items_New

from Helpers import *
import RandomEn
from PIL import Image, ImageTk
import importlib
import pickle
import ttk
"""mostly works but doesnt update the button after refroming the selection menu"""


#NPC_choices={'General NPC':["None"], 'Merchant':["General","Weps", "Armor"
                                              #"Blksmith"], 'Warrior':NPCs.ClassAttr.keys()}

#class_name=StringVar(CC_tab)
#class_name.set("Class Type")

#def uptypes(x,y,z):
    #new_choices = NPC_choices[NPCty_choice.get()]
    #class_select['menu'].delete(0, 'end')
    #for ch in new_choices:
            #class_select['menu'].add_command(label=ch)#, command=class_name.set(ch))    
       

#class_select=OptionMenu(CC_tab, class_name, *NPC_choices["General NPC"])
#class_select.place(x=250, y=350)

#NPCty_choice = StringVar(CC_tab)
#NPCty_choice.trace('w', uptypes)
#NPCty_choice.set("General NPC")

#NPC_type=OptionMenu(CC_tab, NPCty_choice, *NPC_choices.keys())
#NPC_type.place(x=10, y=350)





import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
#probably something wrong with tkinter rather than the code
#even the example code didnt work. 
CC_tab = tk.Tk()
width=1000
length=1000
CC_tab.geometry(str(width)+'x'+str(length)+"+200+200")
f=Figure(figsize=(5,4), dpi=100)
#one graph
a=f.add_subplot(111)
a.plot([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8])

canvas=FigureCanvasTkAgg(f, master=CC_tab)
canvas.show()
canvas.get_tk_widget().place(x=20,y=30)
toolbar = NavigationToolbar2TkAgg(canvas,CC_tab)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

'''for some reason its coming up with 2 windows?'''
'''https://www.youtube.com/watch?v=Zw6M-BnAPP0'''


CC_tab.mainloop()