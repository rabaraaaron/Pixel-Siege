import random

class GameSounds:
    pathToBattleSongs = "Assets\\Sounds\\Battle"
    battleSongs = []
    for i in range(1, 9):
        battleSongs.append(pathToBattleSongs + "\\battle" + str(i) + ".wav")

    def getRandomBattleSong(self):
        print(self.battleSongs)
        i = random.randint(0, 7)
        return self.battleSongs[i]
    