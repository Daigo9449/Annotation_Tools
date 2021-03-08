# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:56:07 2021

@author: Diego Maldonado
"""

import random
import os
import cv2
from matplotlib import pyplot as plt
from glob import glob
from math import floor
import albumentations as A

# Define functions to visualize BB and image
BOX_COLOR = (255, 0, 0) # Red
TEXT_COLOR = (255, 255, 255) # White


def visualize_bbox(img, bbox, class_name, color=BOX_COLOR, thickness=2):
    """Visualizes a single bounding box on the image"""
    x_min, y_min, w, h = bbox
    x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)

    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)

    ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)    
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)
    cv2.putText(
        img,
        text=class_name,
        org=(x_min, y_min - int(0.3 * text_height)),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.35, 
        color=TEXT_COLOR, 
        lineType=cv2.LINE_AA,
    )
    return img


def visualize(image, bboxes, category_ids, category_id_to_name):
    img = image.copy()
    for bbox, category_id in zip(bboxes, category_ids):
        class_name = category_id_to_name[category_id]
        img = visualize_bbox(img, bbox, class_name)
    plt.figure(figsize=(12, 12))
    plt.axis('off')
    plt.imshow(img)
    
    
# Images and annotations to process
image = cv2.imread("Dataset/images/000d13275f39a218.jpg")
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#cv2.imshow("Test", image)
txt = glob("Dataset/labels/000d13275f39a218.txt")

bb = open(txt[0], "r")
lines = bb.readlines()

#List where bb and labels will be saved
bbs = []
category_ids = []

##We will use the mapping from category_id to the class name
#to visualize the class label for the bounding box on the image
category_id_to_name = {"Person": "Person"}

for line in lines:
    coord = line.split()
    category = coord[0]
    x1 = float(coord[1])
    y1 = float(coord[2])
    x2 = float(coord[3])
    y2 = float(coord[4])
    anno = [[x1, y1, x2, y2]]
    bbs.extend(anno)
    # if(category=="Person"):
    #      category_ids.append(0)
    category_ids.append(category)

  
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

random.seed()
transformed = transform(image=image, bboxes=bbs, category_ids=category_ids)

#Save image and annotation
#file_kitti = open(os.path.join(dest, filename), "w")

# os.chdir("Data_Augmentation")
txt_annotation = open("000d13275f39a218_aug.txt", "w")
# txt_annotation.write(transformed["bboxes"])

for bbox, tag in zip(transformed['bboxes'],transformed['category_ids']) :
    list_bbox= list(bbox)
    txt_annotation.writelines([str(tag)," ", str(list_bbox[0])," ", str(list_bbox[1])," ", 
                          str(list_bbox[2])," ", str(list_bbox[3]), "\n"])
    

cv2.imwrite("000d13275f39a21"+"_trans.jpg", transformed["image"])



visualize(
    transformed['image'],
    transformed['bboxes'],
    transformed['category_ids'],
    category_id_to_name,
)

bb.close()
txt_annotation.close()


#cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow("original", image)
# cv2.imshow("transformed", transformed["image"])
