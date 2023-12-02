from common import *

file = open("input.txt", "r")
games = file.readlines()
file.close()

gamestats = []
for game in games:
    game = game.strip()
    gamestats += [parsegame(game)]

def checkpossible(game : GameStats):
    possible = True
    if game.highestred > 12:
        possible = False
    if game.highestgreen > 13:
        possible = False
    if game.highestblue > 14:
        possible = False
    return possible

answer = 0

for game in gamestats:
    if checkpossible(game):
        answer += game.id

print(answer)