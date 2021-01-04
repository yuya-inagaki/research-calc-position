# coding: utf-8
# Tobii eye-tracker のデータから視線データ座標をCSVに抽出するプログラム

import pandas as pd
import os

from file import Csv

# SETTINGS
DATA_PATH = 'data'

def process(file_name):
  print(file_name)

  print('Loading data file')
  df = pd.read_excel(DATA_PATH + '/' + file_name)
  
  for row in df.itertuples():
    event_name = row[76]
    stimules_name = row[68]
    if event_name != 'Fixation' or pd.isnull(stimules_name) or stimules_name == 'black' or stimules_name == 'Eyetracker Calibration':
      continue

    print(stimules_name)
    file_path = DATA_PATH + '/gazedata/' + stimules_name + '.csv'
    Csv(file_path, row)

# Listed directory
files = os.listdir(DATA_PATH)
for file in files:
  if not os.path.isdir(DATA_PATH + "\\" + file) and (file[-4:] == '.xls' or file[-5:] == '.xlsx'):
    process(file)