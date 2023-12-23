import pandas as pd 
import json
import os
import glob
import webbrowser


def read_database(): 

    files=glob.glob("../Lorcana_database/*")

    # load first expansion 
    data=json.load(open(files[0]))  
    cards=pd.DataFrame(data['cards']).set_index('id')
    cards['N_set']=1
    # info about set
    del data['cards']
    set_info=pd.DataFrame([data]) 
    set_info['N_set']=1
    set_info=set_info.set_index('N_set')

#    print(set_info)

    for i in range(1,len(files)): 
        data=json.load(open(files[i]))
        #print(data.keys)
        add_cards=pd.DataFrame(data['cards']).set_index('id')
        add_cards['N_set']=i+1  
         # info about set
        del data['cards']
        set_info_add=pd.DataFrame([data]) 
        set_info_add['N_set']=i+1
        set_info_add=set_info_add.set_index('N_set')

        cards=pd.concat([cards, add_cards])
        set_info=pd.concat([set_info, set_info_add])



    return cards, set_info

def read_my_collection():

    mycards=pd.read_csv('../MyCollection/MyCards.csv', sep=';')


    return mycards

def get_database():

    ## loading the cards 
    set_database, set_info=read_database()
    mycards=read_my_collection()
    cards=pd.merge(set_database, mycards, on='id', how='inner')

    return cards




