# coding: utf-8
import pandas as pd
import fixation as ft
import result as rt
import os

# mode
# 0: all data (default)
# 1: first 5 seconds
# 2: first 3 seconds
# 3: last 5 seconds
# 4: 4 - 6 seconds
# 5: 7 - 10 seconds
# 6: test seconds

# setting
MODE = 6
DATA_PATH = 'data'

# Main Process


def process(file_name):
    print(file_name)

    # setting
    fixation_event = None
    calibration_flag = False
    result = rt.Result()

    print('Loading data file')
    df = pd.read_excel('data/' + file_name)

    for row in df.itertuples():
        fixation = ft.Fixation(row)

        if (fixation.event == 'Eye tracker Calibration end'):
            print('calibration completed')
            calibration_flag = True
        if not calibration_flag:
            continue

        if fixation.is_event():
            print(fixation.event)
            if(fixation.event == 'ImageStimulusStart'):
                fixation_event = ft.FixationEvent(row)
            elif(fixation.event == 'ImageStimulusEnd'):
                if(fixation_event.event_value != 'black'):
                    fixation_position = fixation_event.average_position()

                    # write data on result.xlsx
                    result.add_data(id=fixation_event.get_stimules_id(), participant_name=fixation.participant_name,
                                    fixation_ave_x=fixation_position[0], fixation_ave_y=fixation_position[1])
        else:
            if fixation.is_fixation():
                required_data = True

                if(MODE == 1):
                  if(fixation.timestamp - fixation_event.start_time > 5000):
                    required_data = False
                elif(MODE == 2):
                  if(fixation.timestamp - fixation_event.start_time > 3000):
                    required_data = False
                elif(MODE == 3):
                  if(fixation.timestamp - fixation_event.start_time < 5000):
                    required_data = False
                elif(MODE == 4):
                  if(fixation.timestamp - fixation_event.start_time > 6000 or fixation.timestamp - fixation_event.start_time < 3000):
                    required_data = False
                elif(MODE == 5):
                  if(fixation.timestamp - fixation_event.start_time < 6000):
                    required_data = False
                elif(MODE == 6):
                  if(fixation.timestamp - fixation_event.start_time < 8000):
                    required_data = False
                if(required_data):
                  fixation_event.add_fixation(row)

    result.save_sheet()


# Listed directory
files = os.listdir(DATA_PATH)
for file in files:
    if not os.path.isdir(DATA_PATH + "\\" + file) and (file[-4:] == '.xls' or file[-5:] == '.xlsx'):
        process(file)
