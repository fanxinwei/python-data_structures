

#fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = []

for line in fh:
    list_each = line.split()
    for word in list_each:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
