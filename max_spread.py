__author__ = 'urandu'

# open the weather.dat
# read all the lines in the file
# for each line , get rid of all multiple spaces
# convert each line into a list
# get the spread of each day
# print out the day with the maximum spread and the actual spread

import re

weather_data = 'weather.dat'
weather_data = open(weather_data, 'r')
weather_data = weather_data.readlines()
line_number = 0
max_spread = 0
day_with_max_spread = ''

for line in weather_data:
    if 1 < line_number < weather_data.__len__() - 1:
        line = re.sub(' +', ' ', line).strip()
        line = line.split(' ')
        day = line[0]
        max_temp = int(re.sub('\*', '', line[1]))
        min_temp = int(re.sub('\*', '', line[2]))
        spread = max_temp - min_temp
        if spread > max_spread:
            max_spread = spread
            day_with_max_spread = day

    line_number += 1
print day_with_max_spread, max_spread
