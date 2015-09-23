import math
import re
import time

start_time = time.time()

lines = []
numbers = []

with open('input4999.txt') as input_file:
    key = input_file.readline()
    for input_line in input_file:
        lines.append(input_line)

comma_shift = 0
for line in lines:
    this_open_bracket_position = line.index('(')
    this_close_bracket_position = line.index(')\n')
    try:
        this_comma_position = line.index(', ')
        comma_shift = 2
    except:
        this_comma_position = line.index(',')
        comma_shift = 1
    this_first_number = line[this_open_bracket_position+1:this_comma_position]
    this_second_number = line[this_comma_position+comma_shift:this_close_bracket_position]
    this_numbers = ([float(this_first_number), float(this_second_number)])
    numbers.append(this_numbers)

# Set min distance to large number
min_distance = 1000000000

distances = []

prev_progress = 0.0
print('0.0%')

indexes = [0,0]
progress = 0.0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            this_x_distance = numbers[i][0] - numbers[j][0]
            this_y_distance = numbers[i][1] - numbers[j][1]
            #this_distance = math.sqrt((this_x_distance**2)+(this_y_distance**2))
            this_distance = (this_x_distance**2.0)+(this_y_distance**2.0)
            distances.append(this_distance)
            if this_distance <= min_distance:
                min_distance = this_distance
                indexes = [i, j]
    progress = (float(i)/float(len(numbers)))*100.0
    if progress >= prev_progress + 10.0:
        prev_progress = progress
        print(str(progress) + '%')

print('100.0%')

end_time = time.time()

#with open('output_file.txt', 'w') as output_file:
#    for distance in distances:
#        output_file.write(distance + '\n')

print(lines[indexes[0]] + lines[indexes[1]])
print('min distance: ' + str(min_distance))
print('min(distances): ' + str(min(distances)))
print('time taken: ' + str(end_time-start_time) + 's')