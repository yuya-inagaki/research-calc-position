#
# Fixation Class
#
import pandas as pd
import numpy as np


class Fixation:
    def __init__(self, data):
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
