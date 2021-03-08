# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:39:03 2021

@author: diego
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:20:07 2021

@author: Diego Maldonado
"""

import cv2 
import os
from tqdm import tqdm
from glob import glob
from math import floor
import numpy as np

from facenet_pytorch import MTCNN
from PIL import Image
from matplotlib import pyplot as plt



#Images and annotations extracted from deepstream
txt = glob("annotation/*.txt")
images = glob("annotation/*.png")


#Images and annotations from OpenImage  (for testing purposes only)
txt = glob("Dataset/labels/*.txt")
images = glob("Dataset/images/*.jpg")
           

# Blue color in BGR 
color = (255, 0, 0) 
#color = tuple(np.random.choice(range(256), size=3))
#color = tuple(np.random.randint(256, size=3, dtype=int))

# Line thickness of 2 px 
thickness = 2

# Create face detector
#mtcnn = MTCNN(margin=20, keep_all=False, post_process=False, device='cuda:0')
mtcnn = MTCNN(select_largest=False, keep_all=True, device='cuda')

for image_dir, bb_dir in tqdm(zip(images, txt)): 
        image = cv2.imread(image_dir)
        # cv2.imshow("image", image)      
        # cv2.waitKey(0)
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
            
            roi = image.copy()[floor(float(coord[2])):floor(float(coord[4])), floor(float(coord[1])):floor(float(coord[3]))]
            face = mtcnn(roi) 
            
            if face == None:
                print("No face detected")
            else:
                print("Cara detectada")
            
            # Using cv2.rectangle() method 
            # Draw a rectangle with blue line borders of thickness of 2 px 
            #image = cv2.rectangle(image, start_point, end_point, color, thickness) 

            cv2.imshow("roi", roi)
            cv2.waitKey(0)
        
        cv2.imshow("image", image)      
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        