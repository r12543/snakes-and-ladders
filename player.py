class Player(object):

    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.curr_pos = 0

    def change_curr_pos(self, new_pos):
        self.curr_pos = new_pos

    def is_snake(self, pos):
        for snake in self.board.snakes:
            if snake['start'] == pos:
                return snake['end']

    def is_ladder(self, pos):
        for ladder in self.board.ladders:
            if ladder['start'] == pos:
                return ladder['end']

    def play(self, dice_num):
        prev_pos = self.curr_pos
        if self.curr_pos == 0:
            if dice_num == 1:
                self.curr_pos = 1
        else:
            self.curr_pos += dice_num
            snake_end = self.is_snake(self.curr_pos)
            if snake_end:
                self.curr_pos = snake_end
            ladder_top = self.is_ladder(self.curr_pos)
            if ladder_top:
                self.curr_pos = ladder_top
        if self.curr_pos > self.board.WINNING_POSITION:
            self.curr_pos = prev_pos
        return self.curr_pos

