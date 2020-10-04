# coding: utf-8
import pandas as pd
import fixation as ft

print('Loading data file')
df = pd.read_excel('data/sample/sample.xlsx')

# setting
fixation_event = None
calibration_flag = False

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
            print(fixation_event.event_value)
            print(fixation_event.average_position())
    else:
        if fixation.is_fixation():
            fixation_event.add_fixation(row)
