## count the number of a textbook
file_handle = open('William_shakespeare.txt', 'r')
list = []
count_words = {}
all_words_num = 0
for line in file_handle:
    line = line.rstrip()
    line_list = line.split()
    all_words_num = all_words_num + len(line_list)
    for word in line_list:
        count_words[word] = count_words.get(word,0) + 1


biggest_counts = 10
biggest_word = ''
new_dic = {}
for word, num in count_words.items():
    if num > biggest_counts:
        new_dic[word] = num
#
# print(new_dic)
# print('***********************')
# sort_dic = sorted(new_dic.keys())
# for key in sort_dic:
#     print(key , " : " , new_dic[key])


# Create a list of tuples sorted by index 1 i.e. value field
listofTuples = sorted(new_dic.items() , reverse=True, key=lambda x: x[1])
dic_new = {}
# Iterate over the sorted sequence
for elem in listofTuples :
    print(elem[0] , ":" , elem[1] )
print('The number of words in the textbook is', all_words_num
)
#     dic_new[elem[0]] = elem[1]
# print(dic_new)























# #
# #
# # find the word with biggest number
# file_handle = open('mbox-short.txt', 'r')
# list = []
# counts = {}
# for line in file_handle:
#     line = line.rstrip()
#     if 'From' in line:
#         line_list = line.split()
#         # take out the the email name
#         name = line_list[1]
#         # save in the dictionary: counts and its times
#         counts[name] = counts.get(name, 0) + 1
#     else:
#         continue
# print(counts)
#
# biggest_counts = 0
# biggest_name = ''
# for name, num in counts.items():
#     if num > biggest_counts:
#         biggest_counts = num
#         biggest_name = name
#
# print(biggest_name, biggest_counts)
