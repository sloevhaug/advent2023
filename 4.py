testdata = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
testdata = testdata.split("\n")

file = open('4-input.txt')
lines = file.readlines()

totalPoints = 0

# part 1
for line in lines:
    line = line.replace("\n", "")
    points = 0
    winningNumbers = list(filter(None, line.split(':')[1].split('|')[0].split(" ")))
    availableNumbers = list(filter(None, line.split(':')[1].split('|')[1].split(" ")))

    for i in range(0, len(availableNumbers)):
        if(availableNumbers[i] in winningNumbers):
            if points == 0: points = 1
            else: points = points * 2
    
    totalPoints += points

print("part 1: ", totalPoints)

class Game:
    def __init__(self, gamenumber, winning, available, points):
        self.gamenumber = gamenumber
        self.winning = winning
        self.available = available
        self.points = points

scratchcards = []

gameNumber = 0

for line in lines:

    line = line.replace("\n", "")
    points = 0
    winningNumbers = list(filter(None, line.split(':')[1].split('|')[0].split(" ")))
    availableNumbers = list(filter(None, line.split(':')[1].split('|')[1].split(" ")))

    for i in range(0, len(availableNumbers)):
        if(availableNumbers[i] in winningNumbers):
            points += 1
            
    scratchcards.append(Game(gameNumber, winningNumbers, availableNumbers, points))
    
    gameNumber += 1

copies = []

def runGames(games):
    for game in games:

        extraCards = []
        
        for i in range(1, game.points + 1):
            
            copies.append(scratchcards[game.gamenumber + i])
            extraCards.append(scratchcards[game.gamenumber + i])
       
        runGames(extraCards)

runGames(scratchcards)

print(len(scratchcards) + len(copies))
