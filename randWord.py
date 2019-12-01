import random


def genrt(length):
    s = ""
    for i in range(0, length):
        s = s+chr(random.randrange(97, 123))
    return s


def genrtNum(length):
    s = ""
    for i in range(0, length):
        s = s + str(random.randint(0, 9))
    s = int(s)
    return s
