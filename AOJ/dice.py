class Dice:
    def __init__(self, a):
        self.s1, self.s2, self.s3, self.s4, self.s5, self.s6 = a

    def __repr__(self):
        return ' '.join(map(str, ['(',self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, ')']))

    def move_east(self):
        self.s1, self.s3, self.s6, self.s4 = self.s4, self.s1, self.s3, self.s6

    def move_west(self):
        self.s4, self.s1, self.s3, self.s6 = self.s1, self.s3, self.s6, self.s4

    def move_north(self):
        self.s1, self.s5, self.s6, self.s2 = self.s2, self.s1, self.s5, self.s6

    def move_south(self):
        self.s2, self.s1, self.s5, self.s6 = self.s1, self.s5, self.s6, self.s2

    def move_circle(self):
        self.s2, self.s3, self.s5, self.s4 = self.s4, self.s2, self.s3, self.s5


surfaces = list(map(int, input().split()))
q = int(input())

for i in range(q):
    dice = Dice(surfaces)
    up, front = map(int, input().split())
    if dice.s2 == up:
        dice.move_north()
    elif dice.s3 == up:
        dice.move_west()
    elif dice.s4 == up:
        dice.move_east()
    elif dice.s5 == up:
        dice.move_south()
    elif dice.s6 == up:
        dice.move_south()
        dice.move_south()

    for i in range(4):
        if dice.s2 == front:
            print(dice.s3)
            break
        dice.move_circle()
