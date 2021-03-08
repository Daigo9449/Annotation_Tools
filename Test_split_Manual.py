# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:26:03 2021

@author: Diego Maldonado
"""

import cv2 
import os
import shutil
from tqdm import tqdm
from glob import glob
from math import floor
import numpy as np

#Test split for cualitative comparison

#txt = glob("annotation/*.txt")
#images = glob("annotation/*.png")

txt = glob("G:/Jomar_Dataset/annotation/*.txt")
images = glob("G:/Jomar_Dataset/annotation/*.png")
counter = 0 
# Blue color in BGR 
color = (255, 0, 0) 

# Line thickness of 2 px 
thickness = 2

for image_dir, bb_dir in tqdm(zip(images, txt)): 
        image = cv2.imread(image_dir)
        image_copy = image.copy()    #Copy of image to draw rectangle
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
            image_copy = cv2.rectangle(image, start_point, end_point, color, thickness) 
            #image = cv2.rectangle(image, (107, 4), (761, 764), color, thickness) 
            cv2.imshow(image_dir, image_copy)
    
        key = cv2.waitKey(0)
        if key == 115:   #Is Key "s" is pressed then image is saved
             counter = counter + 1     
             bb.close()
             # Move a file from the directory d1 to d2
             shutil.copy(image_dir, "G:/Jomar_Dataset/test_files")
             shutil.copy(bb_dir, "G:/Jomar_Dataset/test_files")
             print("Imagenes guardadas: ", counter)
            
        cv2.destroyAllWindows()
        