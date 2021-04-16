class Board(object):

    def __init__(self):
        self.MAX_NUM_PLAYERS = 4
        self.WINNING_POSITION = 100
        self.snakes = [{
            'start': 15,
            'end': 3
        }, {
            'start': 24,
            'end': 4
        }, {
            'start': 22,
            'end': 13
        }]
        self.ladders = [{
            'start': 2,
            'end': 14
        }, {
            'start': 6,
            'end': 23
        }, {
            'start': 10,
            'end': 21
        }]
