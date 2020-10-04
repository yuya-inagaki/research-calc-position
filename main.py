# coding: utf-8
import pandas as pd
import fixation as fixation

print('Loading data file')
df = pd.read_excel('data/sample/sample_min.xlsx')

for row in df.itertuples():
    fixation_count = 0
    fixation_test = fixation.Fixation(row)

    if fixation_test.is_event():
        print(fixation_test.event)
    else:
        if fixation_test.is_fixation():
            print(fixation_test.point_x, fixation_test.point_y,
                  fixation_test.stimules_name)
