import pandas as pd 
import json
import os
import glob
import webbrowser
import tkinter as tk
from tkinter import *
import read_database as rd
import functions as fun
import PIL
from PIL import ImageTk, Image
import requests
from io import BytesIO


    ## loading the cards 
set_database, set_info=rd.read_database()
mycards=rd.read_my_collection()




def mainMenu():

    print('Welcome to your lorcana database')
    print("What do you want to do? ")
    print("1. Print the cards you have?")
    print("2. Check for a specific cards?")
    print("3. link to picture id?")

    print("0- Exit")

    while True:

        selection = int(input("Enter a choice: "))

        if(selection == 1):
            cards=pd.merge(set_database, mycards, on='id', how='inner')
            cards.to_csv('../output/All_cards.csv')
            selection=cards[['id', 'fullName', 'Number of copies', 'type']]
            print(selection)
            print("You can find more information in output folder")
            continue
        elif(selection == 2):
            selection=set_database[~set_database.index.isin(mycards['id'])]
            selection.to_csv('../output/missing_cards.csv')
            print(selection[['fullName', 'type']])
            count=selection.fullName.count()
            print("you are missing", count, "cards")
            print("you can find more information in output/missing_cards.csv")
            continue
        elif(selection == 3):
            id_to_select=int(input("Enter an id"))
            images_info=set_database.iloc[id_to_select]['images']
            webbrowser.open(images_info['full'])  # Go to example.com
            continue
        elif(selection == 0):
            print("Goodbye")
            exit
        else:
            print("Invalid choice. Enter '0'-'4'")
            print("")
            mainMenu()


mainMenu()


#w = tk.Tk()
##info=input("What do you want to do?")
##id = input('What is your name?\n')  
#w.title('Your personalized Lorcana database')

## Create object  
  
  
## Add image file 
  
#label1 = Label( w, text = "Welcome to your personalized Lorcana database") 
#label1.pack(pady = 50) 

#label2 = Label( w, text = "Select what you want to do") 
#label2.pack(pady = 50) 

#frame1 = Frame(w) 
#frame1.pack(pady = 20 )  

#button1 = Button( frame1, text = "Check one card from 1 id", command=fun.check_in_database(mycards)) 
#button1.pack(pady = 20) 


#Btn = Button(w, text = "This opens images",command=fun.openweb(images_info['full']))
#Btn.pack()


#w.mainloop()



#images_info=cards.iloc[1]['images']


#webbrowser.open(images_info['full'])  # Go to example.com

#root = Tk()
#link = images_info['full']+'?raw=true'
#response = requests.get(link, verify=False )
#img = Image.open(BytesIO(response.content))

#print(link)
#panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
#root.mainloop()

