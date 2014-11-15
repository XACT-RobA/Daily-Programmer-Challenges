import math

with open('text.txt', 'r') as text_file:
    key = text_file.readline()
    input_text = text_file.read()
    
[COLUMN_COUNT_STR, LINE_WIDTH_STR, SPACE_WIDTH_STR] = key.split(' ')
COLUMN_COUNT = int(COLUMN_COUNT_STR)
LINE_WIDTH = int(LINE_WIDTH_STR)
SPACE_WIDTH = int(SPACE_WIDTH_STR)

paragraphs = input_text.split('\n')
lines = []

for paragraph in paragraphs:
    word_list = paragraph.split(' ')
    words = []
    for word in word_list:
        if len(word) > LINE_WIDTH:
            full_line_count = math.floor(len(word) / (LINE_WIDTH - 1))
            remainder = len(word) % (LINE_WIDTH - 1)
            if remainder > 0:
                remainder_exists = 1
            else:
                remainder_exists = 0
            split_word = [None] * (full_line_count + remainder_exists)
            for i in range(full_line_count):
                split_word[i] = word[((LINE_WIDTH - 1) * i):LINE_WIDTH - 1] + '-'
            if remainder_exists == 1:
                split_word[-1] = word[((LINE_WIDTH - 1) * full_line_count):]
            words = words + split_word
        else:
            words = words + [word]
            
    this_line = ''
    for word in words:
        if len(this_line) + 1 + len(word) <= LINE_WIDTH:
            if len(this_line) > 0:
                this_line = this_line + ' ' + word
            else:
                this_line = word
        elif len(this_line) + 1 + len(word) > LINE_WIDTH:
            lines.append(this_line)
            this_line = word
    lines.append(this_line)
    lines.append('')
    
spaced_lines = []
    
for line in lines:
    if len(line) < LINE_WIDTH:
        diff = LINE_WIDTH - len(line)
        line = line + (' ' * diff)
    spaced_lines.append(line)
    
lines = spaced_lines
    
number_of_lines = len(lines)
max_lines_per_column = int(math.floor(number_of_lines / COLUMN_COUNT)) + 1
lines_remaining = int((number_of_lines - (max_lines_per_column * (COLUMN_COUNT - 1))))
column_lengths = ([max_lines_per_column] * (COLUMN_COUNT - 1)) + [lines_remaining]

columns = [None] * COLUMN_COUNT

for i in range(COLUMN_COUNT):
    this_column = []
    for j in range(column_lengths[i]):
        this_column.append(lines[(max_lines_per_column * i) + j])
    columns[i] = this_column
    
output_lines = [None] * max_lines_per_column

for i in range(max_lines_per_column):
    this_line = ''
    for j in range(COLUMN_COUNT):
        if j < (COLUMN_COUNT - 2):
            this_line = this_line + columns[j][i] + (' ' * SPACE_WIDTH)
        elif j == (COLUMN_COUNT - 2):
            this_line = this_line + columns[j][i]
        elif i < lines_remaining: 
                this_line = this_line + (' ' * SPACE_WIDTH) + columns[j][i]
    output_lines[i] = this_line

with open('output.txt', 'w') as output_file:
    for output_line in output_lines:
        output_file.write(output_line + '\n')
                
