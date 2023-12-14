from typing import List

testinput = "10 13 16 21 30 45"
testdata = testinput.split(" ")
testdataint = []

for data in testdata:
    testdataint.append(int(data))

file = open('9-input.txt')
lines = file.readlines()

total = 0
total2 = 0

def diff(array):
    diffArray: list[int] = []
    for i in range(len(array) - 1):
        current = int(array[i])
        next = int(array[i+1])
        diffArray.append(next - current)
    return diffArray
        
def run(array):
    rounds = [array]
    running = True
    while running:
        latest = diff(rounds[-1])
        rounds.append(latest)
        
        if not any(latest):
            running = False
            
    for i in range(len(rounds), 1, -1):
        differance = int(rounds[i - 2][-1]) + int(rounds[i - 1][-1])
        rounds[i - 2].append(differance)

    return rounds[0][-1]

def runBackwards(array):
    
    rounds = [array]
    running = True
    while running:
        latest = diff(rounds[-1])
        rounds.append(latest)
        
        if not any(latest):
            running = False
            
    for i in range(len(rounds), 1, -1):
        rounds[i - 2].insert(0, rounds[i - 2][0] - rounds[i - 1][0])

    return rounds[0][0]

# part 1
for line in lines:
    line = line.replace("\n", "")
    array = line.split(" ")
    
    total += run(array)

# part 2
for line in lines:
    line = line.replace("\n", "")
    array = line.split(" ")
    intarray = []
    for data in array:
        intarray.append(int(data))
    
    total2 += runBackwards(intarray)

print("part 1: ", total)
print("part 2: ", total2)