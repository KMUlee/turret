from fucking import Turret

class Game():
    def __init__(self):
        self.turret = Turret()
        self.tile = []

    def Setting(self,n,list):
        self.turret.setTurret(n)
        self.turret.setArray(list)

    def newGame(self):
        self.turret.game()
        self.tile = self.turret.tile

    def getCoordinate(self, n, m):
        return self.tile[n][m]

    def getTile(self):
        return self.tile

    def getArray(self):
        return self.turret.getArray()

if __name__ == '__main__':
    game = Game()
    game.Setting(0.2, [20,10])
    game.newGame()
    for i in game.tile:
        print(i)



