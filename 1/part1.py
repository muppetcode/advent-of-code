"""
NOTE TO SELF: READ THE QUESTION
file = open("1/input.txt", "r")
input = str(file.read())
foundIntOne = False
usingNumber = ""
allints = list()
for x in input:
    if x.isdigit() == True and foundIntOne == False:
        usingNumber = x
        foundIntOne = True
    elif x.isdigit() == True and foundIntOne == True:
        usingNumber = usingNumber + x
        print(usingNumber)
        allints.append(int(usingNumber))
        foundIntOne = False
    else:
        continue

print(allints)
print(sum(allints))
"""
# PART ONE:
file = open("1/input.txt", "r")
calibrationValues = list()

for line in file:
    foundNums = list()
    for x in line:
        if x.isdigit() == True:
            foundNums.append(x)
    if len(foundNums) == 1:
        value = int(foundNums[0] + foundNums[0])
        calibrationValues.append(value)
    else:
        value = int(foundNums[0] + foundNums[len(foundNums)-1])
        calibrationValues.append(value)

print(calibrationValues)
print(sum(calibrationValues))