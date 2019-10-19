# 5.2 Write a program that repeatedly prompts a user for
# integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message
# and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    # record the number of time
    if num == "done" : break
    else:
        try:
            num = int(num)
            # print('AAAA')
            ## In the first time, input the number as smallest and largest
            if smallest is None:
                # print('BBB')
                smallest = num
                # print('smallest', smallest)
            if num < smallest:
                smallest = num

            if largest is None:
                largest = num
            if num > largest:
                largest = num
                largest = num

        except:
            print('Invalid input')
            continue

print('Maximum is', largest)
print('Minimum is', smallest)
