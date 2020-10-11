# coding: utf-8
import pandas as pd
import cv2
import numpy as np

print(cv2.__version__)

print('Loading data file')
df = pd.read_excel('result/result.xlsx')

size = 1080, 1920, 3
color01 = (0, 255, 255)
color02 = (255, 0, 255)
color03 = (255, 255, 0)
color04 = (255, 0, 0)
color05 = (0, 255, 0)
color06 = (0, 0, 255)
color07 = (0, 127, 127)

# np.fillで白に埋める
white_img = np.zeros(size, dtype=np.uint8)
white_img.fill(255)

for row in df.itertuples():
    if row[17] == 1:
        cv2.drawMarker(white_img, (int(row[18]), int(row[19])), color01,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 2:
        cv2.drawMarker(white_img, (int(row[18]), int(row[19])), color02,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 3:
        cv2.drawMarker(white_img, (int(row[18]), int(row[19])), color03,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 4:
        cv2.drawMarker(white_img, (int(row[18]), int(row[19])), color04,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 5:
        cv2.drawMarker(white_img, (int(row[18]), int(row[19])), color05,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 6:
        cv2.drawMarker(white_img, (int(row[18]), int(row[19])), color06,
                       markerType=cv2.MARKER_TILTED_CROSS)
    elif row[17] == 7:
        cv2.drawMarker(white_img, (int(row[18]), int(row[19])), color07,
                       markerType=cv2.MARKER_TILTED_CROSS)

cv2.namedWindow("white image", cv2.WINDOW_NORMAL)
cv2.imshow("white image", white_img)
cv2.imwrite('result/test.png', white_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
