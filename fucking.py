import random
class Turret():
    def __init__(self):
        self.turret = 0.3
        self.tile = []
        self.array = []

    def getTile(self):
        return self.tile

    def setTurret(self, n):
        self.turret = n

    def setArray(self, list):
        self.array = list

    def getArray(self):
        return self.array

    def game(self):
        self.tile = []

        for i in range(self.array[0]):
            list = []
            for j in range(self.array[1])   :
                p = random.random()
                if  float(p) < self.turret:
                    list.append("*")
                else:
                    list.append("-")
            self.tile.append(list)

        m = self.array[0]
        n = self.array[1]
        tile = self.tile
        for i in range(m):
            for j in range(n):
                num = 0
                if tile[i][j] == "-":
                    if j != 0 and tile[i][j - 1] == "*":
                        num += 1
                    if j != n - 1 and tile[i][j + 1] == "*":
                        num += 1
                    if i != 0 and tile[i - 1][j] == "*":
                        num += 1
                    if i != 0 and j != 0 and tile[i - 1][j - 1] == "*":
                        num += 1
                    if i != 0 and j != n - 1 and tile[i - 1][j + 1] == "*":
                        num += 1
                    if i != m - 1 and j != 0 and tile[i + 1][j - 1] == "*":
                        num += 1
                    if i != m - 1 and tile[i + 1][j] == "*":
                        num += 1
                    if i != m - 1 and j != n - 1 and tile[i + 1][j + 1] == "*":
                        num += 1
                    tile[i][j] = str(num)

if __name__ == '__main__':
    t = Turret()
    for i in t.tile:
        print(i)
