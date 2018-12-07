import random
class Turret():
    def __init__(self):
        self.turret = 30
        self.tile = []
        self.array = [15,10]

    def getTurrets(self):
        return self.turret

    def getTile(self):
        return self.tile

    def setTurret(self, n):
        self.turret = n

    def setArray(self, list):
        self.array = list

    def getArray(self):
        return self.array

    def game(self):
        self.tile = [['-' for x in range(self.array[1])]for x in range(self.array[0])]
        num = 0
        n = self.array[0]
        m = self.array[1]
        while num < self.turret:
            x = random.randrange(m)
            y = random.randrange(n)
            if self.tile[y][x] != '*':
                self.tile[y][x] = '*'
                num += 1
        self.tile = self.find(self.tile,n,m)

    def find(self, tile,n,m):
        X = [-1,0,1,-1,1,-1,0,1]
        Y = [-1,-1,-1,0,0,1,1,1]
        for y in range(n):
            for x in range(m):
                num = 0
                if tile[y][x] == "-":
                    for i in range(8):
                        if 0 <= x + X[i] <= m - 1 and 0 <= y + Y[i] <= n - 1:
                            if tile[y + Y[i]][x + X[i]] == "*":
                                num += 1
                    tile[y][x] = str(num)
        return tile

if __name__ == '__main__':
    t = Turret()
    for i in t.tile:
        print(i)
