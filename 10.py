file = open('10-input.txt')
lines = file.readlines()

class Coordinate:
    def __init__(self, x, y, pipe):
        self.x = x
        self.y = y
        self.pipe = pipe

grid = []
testGrid = [[".",".",".",".","."],[".","S","-","7","."],[".","|",".","|","."],[".","L","-","J","."],[".",".",".",".","."]]

startPos = None

y = 0
for line in lines:
    line = line.replace("\n", "")
    array = []
    x = 0
    for char in line:
        array.append(char)
        if char == "S": 
            startPos = (x, y)
        x += 1
    grid.append(array)
    y += 1

print(startPos)
def toupleToGrid(grid, touple):
    return grid[touple[1]][touple[0]]

print(toupleToGrid(grid, startPos))

directions = {
"|" : ["S", "N"],
"-" : ["E", "W"],
"L" : ["N", "E"],
"J" : ["N", "W"],
"7" : ["S", "W"],
"F" : ["S", "E"],
"." : [""]
}

def navigate(input):
    if input not in ["N", "S", "E", "W"]: return ValueError
    if input == "S": return (0,1)
    if input == "E": return (1,0)
    if input == "N": return (0,-1)
    if input == "W": return (-1,0)

def getNextPos(currentPos, direction):
    steps = navigate(direction)
    return (currentPos[0] + steps[0], currentPos[1] + steps[1])

def search(grid, startPos, next):
    
    path = [toupleToGrid(grid, startPos)]
    roundTrip = False
    
    currentPos = startPos
    nextDirection = next
    
    while not roundTrip:

        nextPos = getNextPos(currentPos, nextDirection)
        nextTile = toupleToGrid(grid, nextPos)
    
        if nextTile == "S":
            path.append(nextTile)
            roundTrip = True
            break

        possibleDirections = directions[nextTile]

        if getNextPos(nextPos, possibleDirections[0]) == currentPos:
            nextDirection = possibleDirections[1]
        else:
            nextDirection = possibleDirections[0]
                      
        path.append(nextTile)
        currentPos = nextPos
    
    print(path)
    print(len(path)//2)

search(grid, startPos, "N")    

