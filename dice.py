from random import randint


class Dice(object):

    @staticmethod
    def roll():
        return randint(1, 6)
