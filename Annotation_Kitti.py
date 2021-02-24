# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:41:46 2021

@author: Diego Maldonado
"""

import os
from tqdm import tqdm

directory = "Dataset\labels" #Directory where images and labels are saved
dest = "labels_kitti" #Directory where txt files in KITTI format will be stored

########################################### KITTI FORMAT ############################################
# Class Truncated Occludded Alpha Top Left Down Right 3DD1 3DD2 3DD3 3DL1 3DL2 3DL3 Rot Score
# Person    0.00	   0	  0.00   t    l    d    r   0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
#####################################################################################################

tags = {
  "Class": "Person",
  "Trunc": "0.00",
  "Occl": "0",
  "Alpha": "0.00",
  "Top": "0.00",
  "Left": "0.00",
  "Down": "0.00",
  "Right": "0.00", 
  "3DD1": "0.00",
  "3DD2": "0.00",
  "3DD3": "0.00",
  "3DL1": "0.00",
  "3DL2": "0.00",
  "3DL3": "0.00",
  "Rot": "0.00",
  "Score": "0.00"
}

for filename in tqdm(os.listdir(directory)):
    if filename.endswith(".txt"): 
        file_kitti = open(os.path.join(dest, filename), "w")
        #print(os.path.join(directory, filename))
        file = open(os.path.join(directory, filename), "r")
        lines = file.readlines()
        for line in lines:
            words = line.split()
            file_kitti.writelines([tags["Class"]," ", tags["Trunc"], " ", tags["Occl"], " ", 
                                   tags["Alpha"], " ", words[1], " ", words[2], " ",
                                   words[3], " ", words[4], " ", tags["3DD1"],  " ", 
                                   tags["3DD2"], " ", tags["3DD3"], " ", tags["3DL1"], " ", 
                                   tags["3DL2"], " ", tags["3DL3"], " ", tags["Rot"], "\n"])
        file_kitti.close()    
        file.close()




