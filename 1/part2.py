file = open("1/input.txt", "r")

# I'm sure there is a better way to do this. This may be an embarassing one to look back on in the future. I didn't want to import a bunch of prasing libriaries to cheat.
def check(string):
    found = list()
    for x in range(0, len(string)):
        # It may throw a range error near the end of the string
        try:
            # Check for "one" and "1"
            if (string[x] == "o" and string[x+1] == "n" and string[x+2] == "e") or (string[x] == "1"):
                #print("one found")
                found.append("1")
            # Check for "two" and "2"
            elif (string[x] == "t" and string[x+1] == "w" and string[x+2] == "o") or (string[x] == "2"):
                #print("two found")
                found.append("2")
            # Check for "three" and "3"
            elif (string[x] == "t" and string[x+1] == "h" and string[x+2] == "r" and string[x+3] == "e" and string[x+4] == "e") or (string[x] == "3"):
                #print("three found")
                found.append("3")
            # Check for "four" and "4"
            elif (string[x] == "f" and string[x+1] == "o" and string[x+2] == "u" and string[x+3] == "r") or (string[x] == "4"):
                #print("found four")
                found.append("4")
            # Check for "five" and "5"
            elif (string[x] == "f" and string[x+1] == "i" and string[x+2] == "v" and string[x+3] == "e") or (string[x] == "5"):
                #print("found five")
                found.append("5")
            # Check for "six" and "6"
            elif (string[x] == "s" and string[x+1] == "i" and string[x+2] == "x") or (string[x] == "6"):
                #print("six found")
                found.append("6")
            # Check for "seven" and "7"
            elif (string[x] == "s" and string[x+1] == "e" and string[x+2] == "v" and string[x+3] == "e" and string[x+4] == "n") or (string[x] == "7"):
                #print("seven found")
                found.append("7")
            # Check for "eight" and "8"
            elif (string[x] == "e" and string[x+1] == "i" and string[x+2] == "g" and string[x+3] == "h" and string[x+4] == "t") or (string[x] == "8"):
                #print("eight found")
                found.append("8")
            # Check for "nine" and "9"
            elif (string[x] == "n" and string[x+1] == "i" and string[x+2] == "n" and string[x+3] == "e") or (string[x] == "9"):
                #print("nine found")
                found.append("9")
        except:
            continue
    return found

calibrationValues = list()
for line in file:
    foundNums = check(line)
    print(foundNums)
    if len(foundNums) == 1:
        value = int(foundNums[0] + foundNums[0])
        calibrationValues.append(value)
    else:
        value = int(foundNums[0] + foundNums[len(foundNums)-1])
        calibrationValues.append(value)

print(calibrationValues)
print(sum(calibrationValues))

# A masterpeice.