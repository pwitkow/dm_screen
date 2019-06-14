import sys
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff")
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff\Scripts")
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff\Cities")
import Items_New
from Tkinter import *
from Helpers import *
import RandomEn
from PIL import Image, ImageTk
import importlib
import pickle
import ttk
import DM_display 

CC_tab= ttk.Frame(DM_display.nb)
DM_display.nb.add(CC_tab, text='City Creator')
        ##root=Toplevel()
        ##width=1200
        ##length=600
        ##root.geometry(str(width)+'x'+str(length)+"+200+200")
        ##root.title("City Creator")
        ##image = Image.open("C:\Users\Phillip\Desktop\Dnd Stuff\Images\multi-wood.jpg").resize((width,length))
        ##background_image=ImageTk.PhotoImage(image)
        ##background_label = Label(root, image=background_image)
        ##background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        ##label and city entry
        #city_box=Label(root, text="City Name")
        #city_box.place(x=50, y=50)
        #city=Entry(root)
        #city.insert(END, "Ukriah")
        #city.place(x=50, y=70)
        
        ##list Box for city characters
        #list_box_label=Label(App, text="Populace")
        #list_box_label.grid(column= 0, row=2)
        #list_box= Listbox(App, selectmode="BROWSE",height=16)
        #list_box.grid(column= 0, row=3, rowspan=8, sticky=N)
        
        
        
        
        
        
        #root.mainloop()