#
# Fixation Class
#
import pandas as pd
import numpy as np


class Fixation:
    def __init__(self, data):
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


class FixationEvent:
    def __init__(self, data):
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
            return(self.fixation_sum_x / self.fixation_count, self.fixation_sum_y / self.fixation_count)
        else:
            return ((self.fixation_sum_x / self.fixation_count)-99, self.fixation_sum_y / self.fixation_count)

    def get_stimules_id(self):
        if self.stimules_name == 'black':
            return 'black'
        else:
            return self.stimules_name[:6]
