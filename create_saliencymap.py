# coding: utf-8
# CSVの視線データから顕著性マップの生成

from scipy import stats, integrate
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# SETTINGS
DATA_PATH = 'data/gazedata'
OUTPUT_PATH = 'output/groundtruth'

def process(file_name):
  # reset Matplotlib
  plt.clf()
  # load the coordinates file
  x, y = np.loadtxt(DATA_PATH + '/' + file_name, delimiter=",", unpack=True)

  # call the kernel density estimator function
  ax = sns.kdeplot(x/1.345, y/1.345, cmap="gray", shade=True, shade_lowest=True, n_levels=100)

  # plot your KDE
  ax.set_frame_on(False)
  ax.set_aspect('equal')
  plt.xlim(0, 1280)
  plt.ylim(803, 0)
  plt.axis('off')

  # save your KDE to disk
  fig = ax.get_figure()
  fig.savefig(OUTPUT_PATH + '/' + file_name[:-4] + '.png',facecolor='black', transparent=False, bbox_inches='tight', pad_inches=0, dpi=258.2)

# Listed directory
files = os.listdir(DATA_PATH)
for file in files:
  if not os.path.isdir(DATA_PATH + "\\" + file) and (file[-4:] == '.csv'):
    process(file)