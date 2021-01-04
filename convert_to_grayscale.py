# coding: utf-8
# RGB saliency map から grayscale saliency map へ変換

import os
import cv2
import numpy as np
import colorsys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from file import Csv

# SETTINGS
DATA_PATH = 'data/salnet_row'
OUTPUT_PATH = 'output/salnet'

def process(file_name):
  print(file_name)

  img = mpimg.imread(DATA_PATH + '/' + file_name)
  img = img[ : , : , 0:3]
  new_image = np.zeros((img.shape[0], img.shape[1]))
  for y_pos in range(img.shape[0]):
    for x_pos in range (img.shape[1]):
      color = img[y_pos, x_pos]
      r,g,b = color
      h, _, _ = colorsys.rgb_to_hls(r, g, b) 
      new_image[y_pos, x_pos] = 1.0 - h

  # new_image = np.array(new_image, dtype=np.uint8)
  print(new_image.ndim)
  print(new_image)

  img = np.clip(new_image * 255, 0, 255).astype(np.uint8)

  # 線形濃度変換
  gamma = 0.4
  img = img.max() * (img / img.max())**(1/gamma)
  cv2.imwrite(OUTPUT_PATH + '/' + file_name, img)

  # plt.imshow(new_image, cmap='gray')
  # plt.axis('off')
  # plt.savefig(OUTPUT_PATH + '/' + file_name)

# Listed directory
files = os.listdir(DATA_PATH)
for file in files:
  if not os.path.isdir(DATA_PATH + "\\" + file) and (file[-4:] == '.png' or file[-4:] == '.jpg'):
    process(file)