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
f_obj = open(r'D:\FullCSV\New_dataset\tbcov19_tweetids_nort2.txt', 'a', newline='', encoding = 'UTF-8' )
write_obj = csv.writer(f_obj)

# remember to create output jsonl file FIRST

folder = r'D:\FullCSV\New_dataset\file_container2' #folder that contains all jsonl files

for file in os.listdir(folder):
    with pd.read_csv(os.path.join (folder,file), sep='\t', chunksize = 1 ) as f:  
        for line in f:
            
            
            csv_line = []
            id = line.iloc[0][0]
            test = line.iloc[0][4] 
            nonetest = math.isnan(test)

            
            
            if nonetest  is True: #checks for retweet id being null and then writes it to the file

                csv_line.append(id)
                write_obj.writerow(csv_line)
                
            else :
                pass
            

f_obj.close() 


# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:21:52 2022

@author: James
"""

