from GameLogic import Turret

class Game():
    def __init__(self):
        self.turret = Turret()
        self.tile = []

    def Setting(self,n,list):
        self.turret.setTurret(n)
        self.turret.setArray(list)

    def newGame(self):
        self.turret.game()
        self.tile = self.turret.getTile()

    def getCoordinate(self, n, m):
        return self.tile[n][m]

    def setCoordinate(self,n,m,text):
        self.tile[n][m] = text

    def getTile(self):
        return self.tile

    def getArray(self):
        return self.turret.getArray()

    def getTurrets(self):
        return self.turret.getTurrets()

if __name__ == '__main__':
    game = Game()
    game.Setting(0.2, [20,10])
    game.newGame()
    for i in game.tile:
        print(i)



