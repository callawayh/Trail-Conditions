# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 17:33:02 2020

@author: callaway.holt
"""
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime as dt
import os
if str(os.getcwd()) == str(os.getcwd()+"\\Desktop\\Bike-Project") is False:
    os.chdir(os.getcwd()+"\\Desktop\\Bike-Project")
else:
    pass
from get_soup import Data 


# paths 
path = 'https://rainoutline.com/search/extension/9132040204/'

brp = '1'
landhal = '7'
smp = '10'
wyco = '15'
clinton = '18'

parks = [brp,landhal,smp,wyco,clinton]
listy = []
listy2 = []
run_count = 0
while True:
    for x in parks:
        """
        will return the parks data every 5 seconds
        """
        p = path+x
        place = Data(p)
        listy.append(tuple([place.park, place.status]))

        #print(listy)
    dic = dict(listy)
    print('dict 1 ' ,dt.now().minute,dt.now().second)
    print(dic)
    listy.clear()
    time.sleep(5)
    
    for x in parks:
        """
        will return the parks every 10 seconds 
        """
        p = path+x
        place = Data(p)
        listy2.append(tuple([place.park, place.status]))
        run_count += 1
    
    dic2 = dict(listy2)
    print('dict 2 ', dt.now().minute,dt.now().second)
    print(run_count)
    
    # it runs 5 times each loop
    # for testing purposes
    if run_count == 15:
        dic2['Blue River Park'] = "Open"
    print(dic2)
    
    #listy2.clear()
    
    ## This basically checks if it is different than it was ~5 seconds ago
    print(dic == dic2)
    time.sleep(10)
    
    # If the dics dont match that means something changed
    # if the status is open let me know so
    if dic != dic2:
        for key1,key2 in zip(dic, dic2):
            if dic[key1] != dic2[key2]:
                if dic2[key2] == "Open":
                    print('{} is now open'.format(key2))
        break 