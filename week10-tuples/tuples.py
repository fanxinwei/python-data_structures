file_handle = open('mbox-short.txt', 'r')
dic_time = {}
for line in file_handle:
    line_tidy = line.rstrip()
    line_list = line.split()

    if line_list == []:
        continue
    elif line_list[0] == 'From':
        # print(line_list)
        time = line_list[5][:2]
        # print(time)
        dic_time[time] = dic_time.get(time, 0) + 1
        # print(dic_time)
    else:
        continue

tuple_list = []
tuple_list = dic_time.items()
tuple_sorted = sorted(tuple_list)
for time, num in tuple_sorted:
    print(time, num)
