
from random import randint
from itertools import cycle


class Board:
    def __init__(self):
        self._board = [["-"]*3 for i in range(3)]

    def display(self):
        for row in self._board:
            for tile in row:
                if tile != "-":
                    tile = tile.symbol
                print(tile, end=" ")
            print()

    def place_symbol(self, player, tile):
        """Try to place the player inside the tile
        The important thing here is that it returns None if it fails
        """
        row, column = tile
        if self._board[row][column] == "-":
            self._board[row][column] = player
            return True

    def check_win(self):
        """Checks all possible winning combinations,
        Returns True for a win and False otherwise.
        """
        #Store checks here
        checks = set()

        # Add rows
        for row in self._board:
            checks.add(tuple(row))

        # Add columns
        columns = zip(self._board[0], self._board[1], self._board[2])
        for columns in columns:
            checks.add(tuple(columns))

        # Add diagonals
        diag1 = (self._board[0][0], self._board[1][1], self._board[2][2])
        diag2 = (self._board[0][2], self._board[1][1], self._board[2][0])
        checks.update((diag1, diag2))

        # Check every option for a win
        checks = {True if (len(set(lst)) == 1 and lst[0] != "-") else False for lst in checks}
        if True in checks:
            return True
        return False

    def is_full(self):
        if "-" not in (self._board[0]+self._board[1]+self._board[2]):
            return True
        return False


class Player:
    def __init__(self, is_human, symbol, name):
        self.is_human = is_human
        self.symbol = symbol
        self.name = name
        self.score = 0

def get_player_input(choices, text=''):
    while True:
        input = input(text)
        if input in choices:
            return input
        print(f"Enter one of the following: {', '.join(choices)}")


def main():
    print("Welcome to tic tac toe!")
    print("type the appropriate number to choose a game option:")
    print("1.player vs player\n2.player vs computer\n3.computer vs computer")
    choice = get_player_input(('1', '2', '3'),)
    if choice == '1':
        player1_name = input("Choose a Name for player 1: ")
        player2_name = input("Choose a Name for player 2: ")
        player1_is_human = True
        player2_is_human = True
    elif choice == '2':
        player1_name = input("Choose a name: ")
        player2_name = "Computer"
        player1_is_human = True
        player2_is_human = False
    elif choice == '3':
        player1_name = "Computer 1"
        player2_name = "Computer 2"
        player1_is_human = False
        player2_is_human = False

    player1 = Player(player1_is_human, "X", player1_name)
    player2 = Player(player2_is_human, "O", player2_name)
    players = [player1, player2]
    board = Board()
    # For player row and column input
    options = ('1', '2', '3')

    for player in cycle(players):
        board.display()
        print(f"It's {player.name}'s turn")

        # The actual turn of the player
        while True:
            if player.is_human:
                row = int(get_player_input(options, "Enter row number(1-3): ")) - 1
                column = int(get_player_input(options, "Enter column number(1-3): ")) - 1
            else:
                row, column = randint(0, 2), randint(0, 2)

            result = board.place_symbol(player, (row, column))
            if result is None:
                if player.is_human:
                    print("Enter in a non-full tile")
                continue
            else:
                break

        win = board.check_win()
        if win or board.is_full():
            board.display()
            if win:
                print(f"player {player.name} won")
                player.score += 1
                print(f"current scores:\nPlayer {players[0].name}: {players[0].score}")
                print(f"Player {players[1].name}: {players[1].score}")
            elif board.is_full():
                print("It's a draw!")

            again = input("another game?(y/n)")
            if again == "y":
                board = Board()
                continue
            return


if __name__ == '__main__':
    main()