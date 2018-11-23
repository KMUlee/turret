import random
class Turret():
    def __init__(self):
        self.turret = float(input("지뢰"))
        self.array = list(map(int, input("크기").split()))
        self.make()

    def make(self):
        self.tile = []
        for i in range(self.array[0]):
            list = []
            for j in range(self.array[1]):
                p = random.random()
                if  float(p) < self.turret:
                    list.append("*")
                else:
                    list.append("-")
            self.tile.append(list)
        self.find()

    def find(self):
        m = self.array[0]
        n = self.array[1]
        tile = self.tile
        for i in range(m):
            
            for j in range(n):
                num = 0
                if tile[i][j] == "-":

                    if i == 0:
                        if j != 0 and tile[i][j-1] == "*":
                            num += 1
                        if j != n-1 and tile[i][j+1] == "*":
                            num += 1
                        if j != 0 and tile[i+1][j-1] == "*":
                            num += 1
                        if tile[i+1][j] == "*":
                            num += 1
                        if j != n-1 and tile[i+1][j+1] == "*":
                            num += 1

                    elif i == m-1:
                        if j != 0 and tile[i][j-1] == "*":
                            num += 1
                        if j != n-1 and tile[i][j+1] == "*":
                            num += 1
                        if tile[i-1][j] == "*":
                            num += 1
                        if j != 0 and tile[i-1][j-1] == "*":
                            num += 1
                        if j != n-1 and tile[i-1][j+1] == "*":
                            num += 1

                    else:
                        if j != 0 and tile[i][j-1] == "*":
                            num += 1
                        if j != n-1 and tile[i][j+1] == "*":
                            num += 1
                        if tile[i-1][j] == "*":
                            num += 1
                        if j != 0 and tile[i-1][j-1] == "*":
                            num += 1
                        if j != n-1 and tile[i-1][j+1] == "*":
                            num += 1
                        if j != 0 and tile[i+1][j-1] == "*":
                            num += 1
                        if tile[i+1][j] == "*":
                            num += 1
                        if j != n-1 and tile[i+1][j+1] == "*":
                            num += 1
                    tile[i][j] = str(num)

if __name__ == '__main__':
    t = Turret()
    for i in t.tile:
        print(i)