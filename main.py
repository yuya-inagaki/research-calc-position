# coding: utf-8
import pandas as pd
import fixation as ft
import result as rt


print('Loading data file')
df = pd.read_excel('data/Yuya Inagaki - set01 Recording5.xlsx')

# setting
fixation_event = None
calibration_flag = False
result = rt.Result()

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

                result.add_data(id=fixation_event.get_stimules_id(), participant_name=fixation.participant_name,
                                fixation_ave_x=fixation_position[0], fixation_ave_y=fixation_position[1])
    else:
        if fixation.is_fixation():
            fixation_event.add_fixation(row)

result.save_sheet()
