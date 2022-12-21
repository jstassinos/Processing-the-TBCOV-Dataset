# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:56:02 2021

@author: James
"""
import pandas as pd
import csv

import jsonlines
import os
from pprint import pprint


f_obj = open(r'D:\fullcsv\New_dataset\Hydrated_output\Holding_area\tbcov_senti.csv', 'a', newline='', encoding = 'UTF-8' )
write_obj = csv.writer(f_obj)

# remember to create output jsonl file FIRST

folder = r'D:\fullcsv\New_dataset\Hydrated_output\outputs' #folder that contains all jsonl files

object_id = 0

for file in os.listdir(folder):
    with jsonlines.open(os.path.join(folder,file)) as f:
        for line in f.iter():
            
            csv_line = []
            # pprint(line)
            # break
        

            id_str = line['id_str']
            tme = line['date']
            pol = line['polarity']
            sub = line['subjectivity']
            

            hap = line['vader_pos']
            ang = line['vader_neg']
            sur = line['vader_neu']
            sad = line['vader_comp']
            fea = line['afinn']
            
            
            
        
#           text_blob = TextBlob(line['full_text'])
#            line['polarity'] = text_blob.sentiment.polarity
            
            csv_line.append(id_str)
            csv_line.append(tme)
            csv_line.append(pol)
            csv_line.append(sub)
            
            csv_line.append(hap)
            csv_line.append(ang)
            csv_line.append(sur)
            csv_line.append(sad)
            csv_line.append(fea)
            csv_line.append(object_id)
            
            object_id = object_id + 1

            # print(csv_line)
            # break

            write_obj.writerow(csv_line)
f_obj.close() 
