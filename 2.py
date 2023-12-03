testdata = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

file = open('2-input.txt')
document = file.readlines()

redCubes = 12
greenCubes = 13
blueCubes = 14

def analyzeGame(maxRed, maxGreen, maxBlue, gameArray):
    
    sumPossibleGames = 0
    powerOfGames = 0

    maxCubes = {
    'red' : maxRed,
    'green' : maxGreen,
    'blue' : maxBlue,
    }
        
    for game in gameArray:
        game = game.replace('\n', '')
        gameNumber = game.split(":")[0].split(" ")[1]
        picks = game.split(':')[1].split(';')
               
        possible = isGamePossible(maxCubes, gameNumber, picks)
        power = powerOfCubes(picks)

        if possible: 
            sumPossibleGames += int(gameNumber)
        
        powerOfGames += power
    
    return {'sum of games' : sumPossibleGames, 'power of games' : powerOfGames}

def isGamePossible(maxCubes, gameNumber, picks):
    for pick in picks:
        
        cubes = pick.split(",")

        for cube in cubes:
            number = int(cube.split(" ")[1])
            color = cube.split(" ")[2]
            
            if color in maxCubes:
                if maxCubes[color] < number:
                    print("Game: " + gameNumber + " has too many (" + str(number) + ") " + color + " cubes!")
                    return False
    return True

def powerOfCubes(picks):
    minCubes = {
    'red' : 0,
    'green' : 0,
    'blue' : 0,
    }

    for pick in picks:
        cubes = pick.split(",")
        for cube in cubes:
            number = int(cube.split(" ")[1])
            color = cube.split(" ")[2]
            if color in minCubes:
                if minCubes[color] < number:
                    minCubes[color] = number                    

    return minCubes['red'] * minCubes['green'] * minCubes['blue']

print(analyzeGame(maxRed=redCubes, maxGreen=greenCubes, maxBlue=blueCubes, gameArray=document))


# 2634 too high