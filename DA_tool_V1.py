# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:22:13 2021

@author: Diego Maldonado
"""

import random
import os
import cv2
from matplotlib import pyplot as plt
from glob import glob
from math import floor
import albumentations as A
from tqdm import tqdm


# Images and annotations to process
images = glob("D:/Usuarios/diego/Documentos/GitHub/Annotation_Tools/annotation/*.png")
txt = glob("D:/Usuarios/diego/Documentos/GitHub/Annotation_Tools/annotation/*.txt")

#List where bb and labels will be saved
bbs = []
category_ids = []

##We will use the mapping from category_id to the class name
#to visualize the class label for the bounding box on the image
category_id_to_name = {"Person": "Person"}

#Transformation to be applied
transform = A.Compose(
    [A.HorizontalFlip(p=1.0),
     A.Rotate(limit=25, border_mode=cv2.BORDER_CONSTANT, value=1, p=1),
     A.ISONoise(color_shift=(0.01, 0.01), intensity=(0.1, 0.1), p=1.0),
     A.Blur(blur_limit = 5,p=1.0),
     A.RandomBrightnessContrast (brightness_limit=0.2, contrast_limit=0.2, brightness_by_max=True, p=1),
     A.GaussNoise (var_limit=(100.0, 300.0), mean=40, always_apply=False, p=1)
     ],
    bbox_params=A.BboxParams(format='pascal_voc', label_fields=['category_ids']),
)


i = 1;

for image_dir, bb_dir in tqdm(zip(images, txt)): 
        image = cv2.imread(image_dir)
        bb = open(bb_dir, "r")
        lines = bb.readlines()
        for line in lines:
            coord = line.split()
            category = coord[0]
            x1 = float(coord[1])
            y1 = float(coord[2])
            x2 = float(coord[3])
            y2 = float(coord[4])
            anno = [[x1, y1, x2, y2]]
            bbs.extend(anno)
            if(category=="0"):
                  category_ids.append("Person")
            #category_ids.append(category)
        
        random.seed()
        transformed = transform(image=image, bboxes=bbs, category_ids=category_ids)
        
        
        os.chdir("Data_Augmentation")
        # filename_str = str.split(image_dir, "*_")[0]
        # print(image_dir)
        txt_annotation = open("DA"+str(i)+".txt", "w")
        
        for bbox, tag in zip(transformed['bboxes'],transformed['category_ids']) :
            list_bbox= list(bbox)
            txt_annotation.writelines([str(tag)," ", str(list_bbox[0])," ", str(list_bbox[1])," ", 
                                  str(list_bbox[2])," ", str(list_bbox[3]), "\n"])
    

        cv2.imwrite("DA" + str(i) + ".png", transformed["image"])
        
        bbs.clear()
        category_ids.clear()
        
        txt_annotation.close()
        bb.close()
        
        os.chdir("..")
        i=i+1
        