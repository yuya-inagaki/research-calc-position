# coding: utf-8
import pandas as pd
import cv2
import numpy as np

# setting
DATA_FILE_NAME = 'result_all.xlsx'
FOLDER_NAME = 'visual_all'

print(cv2.__version__)
print('Loading data file')
df = pd.read_excel('result/' + DATA_FILE_NAME)

size = 1080, 1920, 3
color = (0, 0, 0)

# np.fillで白に埋める
image_type1 = np.zeros(size, dtype=np.uint8)
image_type2 = np.zeros(size, dtype=np.uint8)
image_type3 = np.zeros(size, dtype=np.uint8)
image_type4 = np.zeros(size, dtype=np.uint8)
image_type5 = np.zeros(size, dtype=np.uint8)
image_type6 = np.zeros(size, dtype=np.uint8)
image_type7 = np.zeros(size, dtype=np.uint8)
image_type1.fill(255)
image_type2.fill(255)
image_type3.fill(255)
image_type4.fill(255)
image_type5.fill(255)
image_type6.fill(255)
image_type7.fill(255)

cv2.putText(image_type1, 'type1', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)
cv2.putText(image_type2, 'type2', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)
cv2.putText(image_type3, 'type3', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)
cv2.putText(image_type4, 'type4', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)
cv2.putText(image_type5, 'type5', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)
cv2.putText(image_type6, 'type6', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)
cv2.putText(image_type7, 'type7', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)

for row in df.itertuples():
    if row[17] == 1:
        cv2.drawMarker(image_type1, (int(row[18]), int(row[19])), color,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 2:
        cv2.drawMarker(image_type2, (int(row[18]), int(row[19])), color,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 3:
        cv2.drawMarker(image_type3, (int(row[18]), int(row[19])), color,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 4:
        cv2.drawMarker(image_type4, (int(row[18]), int(row[19])), color,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 5:
        cv2.drawMarker(image_type5, (int(row[18]), int(row[19])), color,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 6:
        cv2.drawMarker(image_type6, (int(row[18]), int(row[19])), color,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 7:
        cv2.drawMarker(image_type7, (int(row[18]), int(row[19])), color,
                       markerType=cv2.MARKER_TILTED_CROSS)

cv2.imwrite('result/' + FOLDER_NAME + '/type1.png', image_type1)
cv2.imwrite('result/' + FOLDER_NAME + '/type2.png', image_type2)
cv2.imwrite('result/' + FOLDER_NAME + '/type3.png', image_type3)
cv2.imwrite('result/' + FOLDER_NAME + '/type4.png', image_type4)
cv2.imwrite('result/' + FOLDER_NAME + '/type5.png', image_type5)
cv2.imwrite('result/' + FOLDER_NAME + '/type6.png', image_type6)
cv2.imwrite('result/' + FOLDER_NAME + '/type7.png', image_type7)
cv2.waitKey(0)
