inputTime = [58, 99, 64, 69]
inputDistance = [478, 2232, 1019, 1071]

totalPossibilities = 1

def travel(timeLeft, speed):
    return timeLeft * speed
    
def calculatePossibilites(totalTime, recordDistance):
    
    distance = []
    
    for i in range(totalTime):
        distance.append(travel(totalTime - i, i))
        
    result = filter(lambda x: x > recordDistance, distance)
    return len(list(result))
    
for i in range(len(inputTime)):
    totalPossibilities = totalPossibilities * calculatePossibilites(inputTime[i], inputDistance[i])
 
print(totalPossibilities)
print(calculatePossibilites(58996469, 478223210191071))