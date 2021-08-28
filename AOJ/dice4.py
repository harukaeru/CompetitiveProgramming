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


# surfaces2 = list(map(int, input().split()))

def check(dice1, dice2):
    for i in range(4):
        if dice2.s2 == dice1.s2:
            if dice2.s3 == dice1.s3 and dice2.s4 == dice1.s4 and dice2.s5 == dice1.s5 and dice2.s6 == dice1.s6:
                return True
        dice2.move_circle()


def check_same_dice(surfaces1, surfaces2):
    dice1 = Dice(surfaces1)
    dice2 = Dice(surfaces2)

    if dice2.s1 == dice1.s1:
        if check(dice1, dice2):
            return True

    dice2 = Dice(surfaces2)
    if dice2.s2 == dice1.s1:
        dice2.move_north()
        if check(dice1, dice2):
            return True

    dice2 = Dice(surfaces2)
    if dice2.s3 == dice1.s1:
        dice2.move_west()
        if check(dice1, dice2):
            return True

    dice2 = Dice(surfaces2)
    if dice2.s4 == dice1.s1:
        dice2.move_east()
        if check(dice1, dice2):
            return True

    dice2 = Dice(surfaces2)
    if dice2.s5 == dice1.s1:
        dice2.move_south()
        if check(dice1, dice2):
            return True

    dice2 = Dice(surfaces2)
    if dice2.s6 == dice1.s1:
        dice2.move_south()
        dice2.move_south()
        if check(dice1, dice2):
            return True

n = int(input())
surfaces_list = []
for i in range(n):
    surfaces_list.append(list(map(int, input().split())))

for j in range(len(surfaces_list) - 1):
    a_surfaces = surfaces_list[j]

    for b_surfaces in surfaces_list[j+1:]:
        is_same = check_same_dice(a_surfaces, b_surfaces)
        if is_same:
            print('No')
            exit()

print('Yes')
