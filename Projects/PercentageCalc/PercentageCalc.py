# program to calc the foot percentage

def calculation(total, part):
    one_percent = total / 100
    count = round(part / one_percent, 2)
    return count
    


total = int(input("What is the total number?"))
part = int(input("And what is the part number?"))

result = calculation(total, part)
print(str(result)+"% is the percentage of "+str(total)+" of "+str(part))



