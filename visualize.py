# coding: utf-8
import pandas as pd
import cv2
import numpy as np

print(cv2.__version__)

print('Loading data file')
df = pd.read_excel('result/result_2s-1.xlsx')

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

cv2.putText(white_img, 'type1', (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color01, 1, cv2.LINE_AA)
cv2.putText(white_img, 'type2', (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color02, 1, cv2.LINE_AA)
cv2.putText(white_img, 'type3', (10, 90), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color03, 1, cv2.LINE_AA)
cv2.putText(white_img, 'type4', (10, 120), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color04, 1, cv2.LINE_AA)
cv2.putText(white_img, 'type5', (10, 150), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color05, 1, cv2.LINE_AA)
cv2.putText(white_img, 'type6', (10, 180), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color06, 1, cv2.LINE_AA)
cv2.putText(white_img, 'type7', (10, 210), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color07, 1, cv2.LINE_AA)

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
cv2.imwrite('result/visual_4-6.png', white_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
