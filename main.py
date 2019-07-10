import board
import sys


def main():
    game = board.board()
    p_win = 0

    while True:
        while not game.gameOver:
            game.move()
            game.print()
        game.reset()

        new_game = input("Enter 'y' for new game\n")
        if new_game != 'y':
            break


if __name__ =="__main__":
    main()