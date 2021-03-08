# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:44:48 2021

@author: Diego Maldonado
"""

#XML parser

from bs4 import BeautifulSoup
import os 
from glob import glob
from tqdm import tqdm

paths = glob('G:/OD-WeaponDetection-master/Knife_detection/annotations/*.xml') #Path where annotations in XML format are stored
#paths = paths[0:5]
for path in tqdm(paths):
    with open(path, "r") as f: 
        data = f.read()
        bs_data = BeautifulSoup(data, "xml")
        file = bs_data.find_all(["filename"]) 
        filename_str = str.split(file[0].text, ".")[0]
        #print(filename_str)
        os.chdir("labels_txt")
        txt = open(filename_str+".txt", "w")
        objs = bs_data.find_all(["name"])
        bboxs = bs_data.find_all(["xmin", "ymin", "xmax", "ymax"])
        annot = []
        for i in range(len(objs)):
            line = '{0} {1} {2} {3} {4} \n'.format(objs[i].text,
                                                 bboxs[i*4+0].text,
                                                 bboxs[i*4+1].text,
                                                 bboxs[i*4+2].text,
                                                 bboxs[i*4+3].text)
            txt.writelines([line])
        txt.close()
        f.close()
        os.chdir("..")
        
     


        
    