userinput2 = int(input("Input a Number: "))

def sum(userinput2):
    sumnum = 0
    for num2 in range(userinput2):
     sumnum += userinput2
     userinput2 -= 1
    return (sumnum)

def ave(input, sum):
    average = 0
    average = sum/input
    return(average)

newsum = sum(userinput2)
newave = ave(userinput2, newsum)


print("Sum = %d" % newsum)
print("Average = %.1f " % newave)

if userinput2 < newave:
    print("Dwarf")
else:
    print("Not Dwarf")



