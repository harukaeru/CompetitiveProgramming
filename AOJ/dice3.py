class Dice:
    def __init__(self, a):
        self.s1, self.s2, self.s3, self.s4, self.s5, self.s6 = a

    def __repr__(self):
        return ' '.join(map(str, ['(',self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, ')']))

    def move_east(self):
        # 4
        self.s1, self.s3, self.s6, self.s4 = self.s4, self.s1, self.s3, self.s6

    def move_west(self):
        # 3
        self.s4, self.s1, self.s3, self.s6 = self.s1, self.s3, self.s6, self.s4

    def move_north(self):
        # 2
        self.s1, self.s5, self.s6, self.s2 = self.s2, self.s1, self.s5, self.s6

    def move_south(self):
        # 5
        self.s2, self.s1, self.s5, self.s6 = self.s1, self.s5, self.s6, self.s2

    def move_circle(self):
        self.s2, self.s3, self.s5, self.s4 = self.s4, self.s2, self.s3, self.s5


surfaces1 = list(map(int, input().split()))
surfaces2 = list(map(int, input().split()))

dice1 = Dice(surfaces1)

def check():
    for i in range(4):
        if dice2.s2 == dice1.s2:
            if dice2.s3 == dice1.s3 and dice2.s4 == dice1.s4 and dice2.s5 == dice1.s5 and dice2.s6 == dice1.s6:
                print('Yes')
                exit()
        dice2.move_circle()


dice2 = Dice(surfaces2)
if dice2.s1 == dice1.s1:
    check()

dice2 = Dice(surfaces2)
if dice2.s2 == dice1.s1:
    dice2.move_north()
    check()

dice2 = Dice(surfaces2)
if dice2.s3 == dice1.s1:
    dice2.move_west()
    check()

dice2 = Dice(surfaces2)
if dice2.s4 == dice1.s1:
    dice2.move_east()
    check()

dice2 = Dice(surfaces2)
if dice2.s5 == dice1.s1:
    dice2.move_south()
    check()

dice2 = Dice(surfaces2)
if dice2.s6 == dice1.s1:
    dice2.move_south()
    dice2.move_south()
    check()

print('No')
