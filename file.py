# coding: utf-8
import csv

class Csv:
  def __init__(self, file_path: str, data):
    self.file = open(file_path, 'a')
    self.writer = csv.writer(self.file)
    self.writerow([data[79]-99, data[80]])

  def writerow(self ,row):
    self.writer.writerow(row)

  def close(self):
    self.file.close()
