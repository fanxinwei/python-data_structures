import re
sum = 0
# file_handle = open('regex_sum_42_sample.txt')
file_handle = open('regex_sum_52977_homework.txt')
for line in file_handle:
    line_clean_end = line.rstrip()
    num = re.findall('[0-9]+', line_clean_end)
    # print(num)
    for i in num:
        # print('the int num', i)
        sum = int(i) + sum
print('the sum is', sum)
