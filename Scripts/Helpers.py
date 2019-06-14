import sys,random
sys.path.append("C:\Users\Phillip\Desktop\Dnd Stuff\Scripts")
import Helpers, NPCs
import Tkinter as tk
#took out items

#def SpellHelp(spell):
    
    #webbrowser.open("http://ephe.github.io/grimoire/spells/"+spell)
    
    #return "Checking for spell..."

#def FeatHelp():
    
    #webbrowser.open("http://engl393-dnd5th.wikia.com/wiki/Feats")
    
    #return "Opening Feats talble..."    


#def SkillHelp():
    
    #webbrowser.open("http://engl393-dnd5th.wikia.com/wiki/Feats")
        
    #return "Opening Feats talble..."    



#def fuckit():
    
    #webbrowser.open("https://youtu.be/eUFY8Zw0Bag?t=4s")
    
    
def numWord(n):
    if n==0:
        return "zero"
    elif n==1:
        return "one"
    elif n==2:
        return "two"
    elif n==3:
        return "three"
    elif n==4:
        return "four"
    elif n==5:
        return "five"
    elif n==6:
        return "six"
    elif n==7:
        return "seven"
    elif n==8:
        return "eight"
    elif n==9:
        return "nine"
    

class XpCounter:
    def __init__(self, XP):
        self.XP=XP
        
    def addXP(self, amount):
        self.XP+=amount
    
    def subXP(self, amount):
        self.XP=self.XP-amount
    
    def getXP(self):
        return self.XP
    


def factorial(x):
    if x ==1:
        return 1
    return factorial(x-1)*x


class Notes:
    def __init__(self,Text=None):
        self.text=Text
        
    def updateText(self, update):
        self.text=update
    
    def get_Text(self):
        return self.text
    
class dice_roller:
    
    def __init__(self, mast, num=None):
        self.num=num
        self.master=mast
        
        self.number_entry=tk.Entry(self.master, width=10)
        self.read_rolls=tk.Text(self.master, height=1, width=10)
        self.total=tk.Text(self.master, height=1, width=3)
        
        def roll_die():
            self.read_rolls.delete('1.0',tk.END)
            rolls=[random.randint(1,self.num) for i in range(int(self.number_entry.get()))]
            self.read_rolls.insert(tk.END, str(rolls))
            
            self.total.delete('1.0', tk.END)
            self.total.insert(tk.END, sum(rolls))
        
        self.but=tk.Button(self.master, text="Roll " + str(self.num) , command=roll_die)
        
        
    def put_it(self,pos=(30,30), spread=100):
        self.but.place(x=pos[0], y=pos[1])
        self.number_entry.place(x=pos[0]+(spread), y=pos[1])
        
        self.read_rolls.place(x=pos[0]+(spread*2), y=pos[1])
        
        self.total.place(x=pos[0]+(spread*3.5), y=pos[1])