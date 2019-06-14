import sys, csv, os
import re
import webbrowser
os.chdir('C:\Users\Phillip\Desktop\Dnd Stuff\Spells')
path='C:\Users\Phillip\Desktop\Dnd Stuff\Spells'
Bard={}
Cleric={}
Druid={}
Palidin={}
Ranger={}
Sorcerer={}
Warlock={}
Wizard={}

for file in os.listdir(path):
    if file.endswith('csv'):
        gg=csv.DictReader(open(file, 'r+'))
        zero=[]
        one=[]
        two=[]
        three=[]
        four=[]
        five=[]
        six=[]
        seven=[]
        eight=[]
        nine=[]        
        for line in gg:
            if int(line["Level"])==0:
                zero.append(re.sub('(Open in new window)', '', line["Spell"]))
            elif int(line["Level"])==1:
                one.append(re.sub('(Open in new window)', '', line["Spell"]))    
            elif int(line["Level"])==2:
                two.append(re.sub('(Open in new window)', '', line["Spell"]))
            elif int(line["Level"])==3:
                three.append(re.sub('(Open in new window)', '', line["Spell"]))
            elif int(line["Level"])==4:
                four.append(re.sub('(Open in new window)', '', line["Spell"]))
            elif int(line["Level"])==5:
                five.append(re.sub('(Open in new window)', '', line["Spell"]))        
            elif int(line["Level"])==6:
                six.append(re.sub('(Open in new window)', '', line["Spell"]))
            elif int(line["Level"])==7:
                seven.append(re.sub('(Open in new window)', '', line["Spell"]))
            elif int(line["Level"])==8:
                eight.append(re.sub('(Open in new window)', '', line["Spell"]))
            elif int(line["Level"])==9:
                nine.append(re.sub('(Open in new window)', '', line["Spell"]))
         
         #Make dictionary of lists for each class       
        if "Bard" in str(file):
            Bard["zero"]=zero
            Bard["one"]=one
            Bard["two"]=two
            Bard["three"]=three
            Bard["four"]=four
            Bard["five"]=five
            Bard["six"]=six
            Bard["seven"]=seven
            Bard["eight"]=eight
            Bard["nine"]=nine
            
        elif "Druid" in str(file):
            Druid["zero"]=zero
            Druid["one"]=one
            Druid["two"]=two
            Druid["three"]=three
            Druid["four"]=four
            Druid["five"]=five
            Druid["six"]=six
            Druid["seven"]=seven
            Druid["eight"]=eight
            Druid["nine"]=nine
            
        elif "Cleric" in str(file):
            Cleric["zero"]=zero
            Cleric["one"]=one
            Cleric["two"]=two
            Cleric["three"]=three
            Cleric["four"]=four
            Cleric["five"]=five
            Cleric["six"]=six
            Cleric["seven"]=seven
            Cleric["eight"]=eight
            Cleric["nine"]=nine 
        
        elif "Palidin" in str(file):
            Palidin["zero"]=zero
            Palidin["one"]=one
            Palidin["two"]=two
            Palidin["three"]=three
            Palidin["four"]=four
            Palidin["five"]=five
            Palidin["six"]=six
            Palidin["seven"]=seven
            Palidin["eight"]=eight
            Palidin["nine"]=nine 
        
        elif "Ranger" in str(file):
            Ranger["zero"]=zero
            Ranger["one"]=one
            Ranger["two"]=two
            Ranger["three"]=three
            Ranger["four"]=four
            Ranger["five"]=five
            Ranger["six"]=six
            Ranger["seven"]=seven
            Ranger["eight"]=eight
            Ranger["nine"]=nine             

        elif "Sorcerer" in str(file):
            Sorcerer["zero"]=zero
            Sorcerer["one"]=one
            Sorcerer["two"]=two
            Sorcerer["three"]=three
            Sorcerer["four"]=four
            Sorcerer["five"]=five
            Sorcerer["six"]=six
            Sorcerer["seven"]=seven
            Sorcerer["eight"]=eight
            Sorcerer["nine"]=nine             
        
        elif "Warlock" in str(file):
            Warlock["zero"]=zero
            Warlock["one"]=one
            Warlock["two"]=two
            Warlock["three"]=three
            Warlock["four"]=four
            Warlock["five"]=five
            Warlock["six"]=six
            Warlock["seven"]=seven
            Warlock["eight"]=eight
            Warlock["nine"]=nine                         
        
        elif "Wizard" in str(file):
            Wizard["zero"]=zero
            Wizard["one"]=one
            Wizard["two"]=two
            Wizard["three"]=three
            Wizard["four"]=four
            Wizard["five"]=five
            Wizard["six"]=six
            Wizard["seven"]=seven
            Wizard["eight"]=eight
            Wizard["nine"]=nine                         



