score = input("Enter Score: ")
try:
    sco = float(score)
except:
    print("The input number is incorrect!")
    quit()

if sco >= 0.9:
    print("A")
elif sco >= 0.8 and sco < 0.9:
    print("B")
elif sco < 0.8 and sco >= 0.7:
    print("C")
elif sco < 0.7 and sco >= 0.6:
    print("D")
else:
    print("F")
