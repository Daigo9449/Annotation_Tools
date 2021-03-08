# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:54:29 2021

@author: Diego Maldonado
"""

import cv2 
import os
import shutil
from tqdm import tqdm
from glob import glob
from math import floor
import numpy as np

## Cleaning tool: Moves to de bad_dir folder the images with bad indexing in their corresponding bounding boxes

#directory = "Dataset\labels" #Directory where images and labels are saved
directory = "Vis_Demo" #Directory where images and labels are saved
directory = "annotation"

#txt = glob("annotation/*.txt")
#images = glob("annotation/*.png")

txt = glob("G:/Jomar_Dataset/annotation/*.txt")
images = glob("G:/Jomar_Dataset/annotation/*.png")

#bad images directory
bad_dir = "G:\Jomar_Dataset\bad_files"

# Blue color in BGR 
color = (255, 0, 0) 
#color = tuple(np.random.choice(range(256), size=3))

#color = tuple(np.random.randint(256, size=3, dtype=int))

# Line thickness of 2 px 
thickness = 2

for image_dir, bb_dir in tqdm(zip(images, txt)): 
        #image = cv2.imread(image_dir)
        bb = open(bb_dir, "r")
        lines = bb.readlines()
        
        for line in lines:
            coord = line.split()
            # Start coordinate 
            # represents the top left corner of rectangle
            try:
                start_point = (floor(float(coord[1])), floor(float(coord[2]))) 
              
            # Ending coordinate 
            # represents the bottom right corner of rectangle 
                end_point = (floor(float(coord[3])), floor(float(coord[4]))) 
            
            except:
                print("Index Error: \n", image_dir)
                bb.close()
                # Move a file from the directory d1 to d2
                shutil.move(image_dir, "G:/Jomar_Dataset/bad_files")
                shutil.move(bb_dir, "G:/Jomar_Dataset/bad_files")

                continue
            
            # Using cv2.rectangle() method 
            # Draw a rectangle with blue line borders of thickness of 2 px 
            
            #image = cv2.rectangle(image, start_point, end_point, color, thickness) 
            #cv2.imshow(image_dir, image)
    
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        




