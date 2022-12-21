# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:42:42 2022

@author: James
"""
import pandas as pd
import csv
import jsonlines
import os
from pprint import pprint
import math



# In[40]:
f_obj = open(r'D:\FullCSV\New_dataset\userlocs\newuserlocs5.csv', 'a', newline='', encoding = 'UTF-8' )
write_obj = csv.writer(f_obj)

# remember to create output jsonl file FIRST

folder = r'D:\FullCSV\New_dataset\file_container' #folder that contains all jsonl files

for file in os.listdir(folder):
    with pd.read_csv(os.path.join (folder,file),  sep='\t', skiprows = 7500000 , chunksize = 1 ) as f:  # open(os.path.join (folder,file)) as f:
        for line in f:
 
            csv_line = []

            test = line.iloc[0][4] 
            nonetest = math.isnan(test)

            if nonetest  is True:

                id = line.iloc[0][0]
                csv_line.append(id)      
                
                senticonf = line.iloc[0][7]
                senti = line.iloc[0][8]
  
                geo_state = line.iloc[0][14]
                geo_county = line.iloc[0][15]
                geo_county_nonetest = pd.isna(geo_county)
                geo_state_nonetest = pd.isna(geo_state)
                
                place_state = line.iloc[0][19] 
                place_county = line.iloc[0][20] 
                place_county_nonetest = pd.isna(place_county)
                place_state_nonetest = pd.isna(place_state)
                         
                userloc_state = line.iloc[0][24] 
                userloc_county = line.iloc[0][25] 
                userloc_county_nonetest = pd.isna(userloc_county)
                userloc_state_nonetest = pd.isna(userloc_state)
                
                if userloc_county_nonetest is False :

                    cprimary_state = userloc_state
                    cprimary_county = userloc_county
                    cprimary_source = "userloc"
                    
                               
                if place_county_nonetest is False :

                    cprimary_state = place_state
                    cprimary_county = place_county
                    cprimary_source = "place"
            
                
                if geo_county_nonetest is False  :

                    cprimary_state = geo_state
                    cprimary_county = geo_county
                    cprimary_source = "geo" 

                
                
                if geo_state_nonetest is True and place_county_nonetest is True and userloc_county_nonetest is True  :
 
           
                    
                    if userloc_state_nonetest is False :

                        cprimary_state = userloc_state
                        cprimary_source = "userloc"
                        cprimary_county = ""
                               
                    if place_state_nonetest is False :

                        cprimary_state = place_state
                        cprimary_source = "place"
                        cprimary_county = ""
                
                    if geo_state_nonetest is False  :

                        cprimary_state = geo_state
                        cprimary_county = ""
                        cprimary_source = "geo" 
         
                if geo_state_nonetest is True and place_county_nonetest is True and userloc_county_nonetest is True and geo_state_nonetest is True and place_state_nonetest is True and userloc_state_nonetest is True :
 
                    cprimary_state = ""
                    cprimary_county = ""
                
                

                csv_line.append(senticonf)
                csv_line.append(senti)
                csv_line.append(cprimary_source)
                csv_line.append(cprimary_state)
                csv_line.append(cprimary_county)




                write_obj.writerow(csv_line)
                
            else :
                pass
           

f_obj.close() 










