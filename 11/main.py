with open("input.txt") as f:
    with open("output.txt", "w") as f1:
        for line in f:
            if "ROW" in line:
                f1.write(line) 

# Expand galaxy

WIDTH = 140
LENGTH = 140

# Rows

"""
for x, line in enumerate(galaxyFile):
    if "#" in line:
        continue
    else:
        contents.insert(x+1, "............................................................................................................................................")
"""