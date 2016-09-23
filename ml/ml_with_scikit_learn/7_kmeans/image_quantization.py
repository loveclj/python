#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: image_quantization.py
@time: 9/23/16 6:07 PM
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle

ogrinal_img = cv2.imread('/home/lizhifeng/Desktop/cat.jpg', flags=True)/255.0
# print ogrinal_img

width, height, depth = tuple(ogrinal_img.shape)

image_flattened = np.reshape(ogrinal_img, (width*height, depth))
image_array_sample = shuffle(image_flattened, random_state=0)[:1000]
estimator = KMeans(n_clusters=64, random_state=0)
estimator.fit(image_array_sample)
cluster_assignments = estimator.predict(image_flattened)

print cluster_assignments.shape

compressed_paltette = estimator.cluster_centers_
compressd_img = np.zeros((width, height, compressed_paltette.shape[1]))

label_index = 0
for i in range(width):
    for j in range(height):
        compressd_img[i][j] = compressed_paltette[cluster_assignments[label_index]]
        label_index += 1



cv2.imshow('cat', compressd_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
if __name__ == '__main__':
    pass