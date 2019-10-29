fh = open('mbox-short.txt')
# count number of lines in the text
num_l = 0
num_num =0
sum = 0
for lx in fh:
    ly = lx.strip()
    num_l = num_l + 1
    if not lx.startswith("X-DSPAM-Confidence:") :
        continue
    else:
# draw the number from the lines with the begin of 'X-DSPAM-Confidence'
        get_num = lx[20:]
        num_num = num_num + 1
        sum = float(sum) + float(get_num)
avg = sum / float(num_num)
print('Average spam confidence:', avg)
