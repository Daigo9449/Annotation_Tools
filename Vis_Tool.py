# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:20:07 2021

@author: Diego Maldonado
"""

import cv2 
import os
import shutil
from tqdm import tqdm
from glob import glob
from math import floor
import numpy as np


#directory = "Dataset\labels" #Directory where images and labels are saved
directory = "Vis_Demo" #Directory where images and labels are saved
directory = "annotation"

#txt = glob("annotation/*.txt")
#images = glob("annotation/*.png")

txt = glob("G:/Jomar_Dataset/annotation/*.txt")
images = glob("G:/Jomar_Dataset/annotation/*.png")

txt =glob("D:/Usuarios/diego/Documentos/GitHub/Annotation_Tools/Data_Augmentation/*.txt")
images =glob ("D:/Usuarios/diego/Documentos/GitHub/Annotation_Tools/Data_Augmentation/*.png")

# Blue color in BGR 
color = (255, 0, 0) 
#color = tuple(np.random.choice(range(256), size=3))

#color = tuple(np.random.randint(256, size=3, dtype=int))

# Line thickness of 2 px 
thickness = 2

for image_dir, bb_dir in tqdm(zip(images, txt)): 
        image = cv2.imread(image_dir)
        bb = open(bb_dir, "r")
        lines = bb.readlines()
        for line in lines:
            coord = line.split()
            # Start coordinate 
            # represents the top left corner of rectangle 
            start_point = (floor(float(coord[1])), floor(float(coord[2]))) 
              
            # Ending coordinate 
            # represents the bottom right corner of rectangle 
            end_point = (floor(float(coord[3])), floor(float(coord[4]))) 
             
            # Using cv2.rectangle() method 
            # Draw a rectangle with blue line borders of thickness of 2 px 
            image = cv2.rectangle(image, start_point, end_point, color, thickness) 
            #image = cv2.rectangle(image, (107, 4), (761, 764), color, thickness) 
            cv2.imshow(image_dir, image)
        bb.close()
    
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        


