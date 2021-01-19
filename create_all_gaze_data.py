# coding: utf-8
# Tobii eye-tracker のデータから視線データ座標をCSVに抽出するプログラム

import pandas as pd
import os
import sys

from file import Csv

# SETTINGS
DATA_PATH = 'data'

def process(file_name, times):
  times = times.split(',')
  print(file_name)

  print('Loading data file')
  df = pd.read_excel(DATA_PATH + '/eye-tracker/' + file_name)
  stumules_start_time = 0
  
  for row in df.itertuples():
    event_name = row[76]
    stimules_name = row[68]

    if row[34] == 'ImageStimulusStart':
      stumules_start_time = int(row[1])

    if event_name != 'Fixation' or pd.isnull(stimules_name) or stimules_name == 'black' or stimules_name == 'Eyetracker Calibration':
      continue
    
    if not ((int(row[1]) - stumules_start_time) > int(times[0]) and (int(row[1]) - stumules_start_time) <= int(times[1])):
      continue

    print(stimules_name)
    # 全て同一ファイルに書き出す
    file_path = DATA_PATH + '/gazedata/all_' + times[0] + '-' + times[1] + '.csv'
    Csv(file_path, row)

# Listed directory
files = os.listdir(DATA_PATH + '/eye-tracker')
for file in files:
  if not os.path.isdir(DATA_PATH + "\\" + file) and (file[-4:] == '.xls' or file[-5:] == '.xlsx'):
    process(file, sys.argv[1])