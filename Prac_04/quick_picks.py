import random

NUMBERS = 6
MIN = 1
MAX = 45


def main():

    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("That makes no sense!")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        quick_pick = []
        for j in range(NUMBERS):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
