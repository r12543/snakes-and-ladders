from board import Board
from dice import Dice
from player import Player

board = Board()

p1 = Player('red', board)
p2 = Player('green', board)

dice = Dice()


found_winner = False
winner = None

while not found_winner:
    n = dice.roll()
    print("Dice for P1: ", n)
    p1_pos = p1.play(n)
    print("P1 position: ", p1_pos)
    if p1_pos == board.WINNING_POSITION:
        found_winner = True
        winner = 'Player 1'
        break

    n = dice.roll()
    print("Dice for P2: ", n)
    p2_pos = p2.play(n)
    print("P2 position: ", p2_pos)
    if p2_pos == board.WINNING_POSITION:
        found_winner = True
        winner = 'Player 2'
        break

if winner is not None:
    print('The winner is: ', winner)
else:
    print('Something went wrong!!! :(')
