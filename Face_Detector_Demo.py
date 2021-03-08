# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:40:13 2021

@author: diego
"""

from facenet_pytorch import MTCNN
import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from tqdm.notebook import tqdm


# Create face detector
mtcnn = MTCNN(margin=150, keep_all=False, post_process=False, device='cuda:0')

#image = cv2.imread("annotation/1_8775.png")
#image = cv2.imread("annotation/1_8730.png")
image = cv2.imread("Vis_Demo/00bfefa51a93b61f.jpg")


# Detect face
face = mtcnn(image)


# Visualize
# fig, axes = plt.subplots(1, len(faces))
# for face, ax in zip(faces, axes):
#     ax.imshow(face.permute(1, 2, 0).int().numpy())
#     ax.axis('off')
# fig.show()

# Visualize
plt.imshow(face.permute(1, 2, 0).int().numpy())
plt.axis('off');


# plt.imshow(face.permute(1, 2, 0).int().numpy())
# plt.axis('off');


# Detect face
boxes, probs, landmarks = mtcnn.detect(image, landmarks=True)

# Visualize
fig, ax = plt.subplots(figsize=(16, 12))
ax.imshow(image)
ax.axis('off')

for box, landmark in zip(boxes, landmarks):
    ax.scatter(*np.meshgrid(box[[0, 2]], box[[1, 3]]))
    ax.scatter(landmark[:, 0], landmark[:, 1], s=8)
fig.show()