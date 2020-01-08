# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:11:06 2019

@author: callaway
"""
# packages 
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime as dt

# paths 
path = 'https://rainoutline.com/search/extension/9132040204/'

brp = '1'
landhal = '7'
smp = '10'
wyco = '15'
clinton = '18'

# make this object oriented and print out the object.park etc
class Data:
    def __init__(self,path):
        self.path = path
        self.source = requests.get(path).text
        self.soup = BeautifulSoup(self.source,'lxml')
        self.park = self.soup.find('div',class_ = 'extensionName').text.rstrip().lstrip()
        self.status = self.soup.find('span', class_ = 'status2').text
        
