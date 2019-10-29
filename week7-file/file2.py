n = 0
file_handle = open('mbox-short.txt', 'r')
for line_string in file_handle:
    line_string_tidy = line_string.rstrip()
    line_list = line_string_tidy.split()

    if len(line_list) == 0 or line_list[0] != 'From':
        continue
    else:
        n = n + 1
        print(line_list[1])
print('There were', n, 'lines in the file with From as the first word')
