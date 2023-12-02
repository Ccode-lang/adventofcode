from common import *

file = open("input.txt", "r")
games = file.readlines()
file.close()

gamestats = []
for game in games:
    game = game.strip()
    gamestats += [parsegame(game)]

def getpower(game : GameStats):
    return game.highestred * game.highestgreen * game.highestblue

answer = 0

for game in gamestats:
    answer += getpower(game)

print(answer)