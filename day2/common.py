class GameStats:
    def __init__(self, id : int, red : list, green : list, blue : list):
        self.id = id
        self.highestred = self.gethighest(red)
        self.highestgreen = self.gethighest(green)
        self.highestblue = self.gethighest(blue)
    def gethighest(self, nums : list):
        bignum = 0
        for num in nums:
            if num > bignum:
                bignum = num
        return bignum
    
def parsegame(game : str):
    id = int(game.split(":")[0].split(" ")[1])
    red = getentriesofcolor("red", game)
    green = getentriesofcolor("green", game)
    blue = getentriesofcolor("blue", game)
    stats = GameStats(id, red, green, blue)
    return stats

def getentriesofcolor(color : str, game : str):
    entries = game.split(":")[1].replace(";", ",").strip().split(", ")
    data = []
    for entry in entries:
        splitentry = entry.split(" ")
        if splitentry[1] == color:
            data += [int(splitentry[0])]
    return data