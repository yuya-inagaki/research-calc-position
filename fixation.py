# coding: utf-8
#
# Fixation Class
#
import pandas as pd
import numpy as np
import cv2


class Fixation:
  def __init__(self, data):
    self.timestamp = data[1]
    self.participant_name = data[4]
    self.event = data[34]
    self.event_value = data[35]
    self.stimules_name = data[68]
    self.media_name = data[69]
    self.eye_movement_type = data[76]
    self.point_x = data[79]
    self.point_y = data[80]

  def is_event(self):
    return not pd.isnull(self.event)

  def is_fixation(self):
    return self.eye_movement_type == 'Fixation'
    # ToDo Consider include not only Fixation but also Saccade event


class FixationEvent:
  def __init__(self, data):
    self.start_time = data[1]
    self.event_value = data[35]
    self.stimules_name = ''
    self.fixation_count = 0
    self.fixation_sum_x = 0
    self.fixation_sum_y = 0

  def add_fixation(self, data):
    self.fixation_count += 1
    self.fixation_sum_x += data[79]
    self.fixation_sum_y += data[80]
    if self.stimules_name == '':
      self.stimules_name = data[68]

  def average_position(self):
    if self.event_value == 'black':
      if self.fixation_count == 0:
        return ('error', 'error')
      else:
        return(self.fixation_sum_x / self.fixation_count, self.fixation_sum_y / self.fixation_count)
    else:
      if self.fixation_count == 0:
        return ('error', 'error')
      else:
        return ((self.fixation_sum_x / self.fixation_count)-99, self.fixation_sum_y / self.fixation_count)

  def get_stimules_id(self):
    if self.stimules_name == 'black':
      return 'black'
    else:
      return self.stimules_name[:6]

class TypeCollection:
  pickup_color = (255, 0, 255)
  def __init__(self, element_type: str, color: object, size: object):
    self.element_type = element_type
    self.color = color
    self.canvas = np.zeros(size, dtype=np.uint8)
    self.canvas.fill(255)
    self.sum_coordinate_x = 0
    self.sum_coordinate_y = 0
    self.min_coordinate_x = size[0]
    self.max_coordinate_x = 0
    self.min_coordinate_y = size[1]
    self.max_coordinate_y = 0
    self.number_of_coordinates = 0
    cv2.putText(self.canvas, element_type, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)

  # 座標の追加
  def AddCenterPoint(self, coordinate_x: float, coordinate_y: float):
    self.sum_coordinate_x += coordinate_x
    self.sum_coordinate_y += coordinate_y
    self.number_of_coordinates += 1
    if self.min_coordinate_x > coordinate_x:
      self.min_coordinate_x = coordinate_x
    if self.max_coordinate_x < coordinate_x:
      self.max_coordinate_x = coordinate_x
    if self.min_coordinate_y > coordinate_y:
      self.min_coordinate_y = coordinate_y
    if self.max_coordinate_y < coordinate_y:
      self.max_coordinate_y = coordinate_y
    self.__DrawCenterPoint(coordinate_x, coordinate_y)
    return (coordinate_x, coordinate_y)

  # マーカーの描写
  def VisualizeMarker(self):
    self.__DrawAveragePoint()
    print('タイプ：' + self.element_type)
    print('中心点' + str(self.__GetAveragePoint()))
    print('半径' + str(self.__GetDenseAreaRadius()))

  # 中心点の取得
  def __GetAveragePoint(self) -> tuple:
    average_x = self.sum_coordinate_x/self.number_of_coordinates
    average_y = self.sum_coordinate_y/self.number_of_coordinates
    return (average_x, average_y)

  # 密集直径の取得
  def __GetDenseAreaRadius(self) -> tuple:
    # mode 1:近い方を半径, 2:平均を半径
    MODE = 2

    radius_x = radisu_y = 0
    if MODE == 1:
      if self.max_coordinate_x - self.__GetAveragePoint()[0] > self.__GetAveragePoint()[0] - self.min_coordinate_x:
        radius_x = self.__GetAveragePoint()[0] - self.min_coordinate_x
      else:
        radius_x = self.max_coordinate_x - self.__GetAveragePoint()[0]
        
      if self.max_coordinate_y - self.__GetAveragePoint()[1] > self.__GetAveragePoint()[1] - self.min_coordinate_y:
        radius_y = self.__GetAveragePoint()[1] - self.min_coordinate_y
      else:
        radius_y = self.max_coordinate_y - self.__GetAveragePoint()[1]
    elif MODE == 2:
      radius_x = ((self.max_coordinate_x - self.__GetAveragePoint()[0]) + (self.__GetAveragePoint()[0] - self.min_coordinate_x)) / 2
      radius_y = ((self.max_coordinate_y - self.__GetAveragePoint()[1]) + (self.__GetAveragePoint()[1] - self.min_coordinate_y)) / 2
    return (radius_x, radius_y)

  # 座標の描写
  def __DrawCenterPoint(self, coordinate_x: float, coordinate_y: float):
    cv2.drawMarker(self.canvas, (int(coordinate_x), int(coordinate_y)), self.color, markerType=cv2.MARKER_TILTED_CROSS)

  # 平均座標の描写
  def __DrawAveragePoint(self):
    cv2.drawMarker(self.canvas, (tuple(map(int,self.__GetAveragePoint()))), TypeCollection.pickup_color, markerType=cv2.MARKER_STAR, markerSize=30)
    cv2.ellipse(self.canvas, (tuple(map(int,self.__GetAveragePoint())), (tuple(map(lambda x: int(x*2),self.__GetDenseAreaRadius()))), 0), TypeCollection.pickup_color)
