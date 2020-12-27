# coding: utf-8
import pandas as pd
import cv2
import numpy as np
from fixation import TypeCollection

# setting
DATA_FILE_NAME = 'result_2s-1.xlsx'
FOLDER_NAME = 'visual_2s-1'

print(cv2.__version__)
print('Loading data file')
df = pd.read_excel('result/' + DATA_FILE_NAME)

size = 1080, 1920-99*2, 3
color = (0, 0, 0)

type1 = TypeCollection('type1', color, size)
type2 = TypeCollection('type2', color, size)
type3 = TypeCollection('type3', color, size)
type4 = TypeCollection('type4', color, size)
type5 = TypeCollection('type5', color, size)
type6 = TypeCollection('type6', color, size)
type7 = TypeCollection('type7', color, size)

for row in df.itertuples():
  if row.type == 1:
    type1.AddCenterPoint(row.average_x, row.average_y)
  if row.type == 2:
    type2.AddCenterPoint(row.average_x, row.average_y)
  if row.type == 3:
    type3.AddCenterPoint(row.average_x, row.average_y)
  if row.type == 4:
    type4.AddCenterPoint(row.average_x, row.average_y)
  if row.type == 5:
    type5.AddCenterPoint(row.average_x, row.average_y)
  if row.type == 6:
    type6.AddCenterPoint(row.average_x, row.average_y)
  if row.type == 7:
    type7.AddCenterPoint(row.average_x, row.average_y)

type1.VisualizeMarker()
type2.VisualizeMarker()
type3.VisualizeMarker()
type4.VisualizeMarker()
type5.VisualizeMarker()
type6.VisualizeMarker()
type7.VisualizeMarker()

cv2.imwrite('result/' + FOLDER_NAME + '/type1.png', type1.canvas)
cv2.imwrite('result/' + FOLDER_NAME + '/type2.png', type2.canvas)
cv2.imwrite('result/' + FOLDER_NAME + '/type3.png', type3.canvas)
cv2.imwrite('result/' + FOLDER_NAME + '/type4.png', type4.canvas)
cv2.imwrite('result/' + FOLDER_NAME + '/type5.png', type5.canvas)
cv2.imwrite('result/' + FOLDER_NAME + '/type6.png', type6.canvas)
cv2.imwrite('result/' + FOLDER_NAME + '/type7.png', type7.canvas)
cv2.destroyAllWindows()
