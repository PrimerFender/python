import random


class TicTacToe:
    def __init__(self):
        self.game_state = [["", "", "", ""], ["", "_", "_", "_"], ["", "_", "_", "_"], ["", "_", "_", "_"]]
        self.start_menu()

    def get_initial_game_state(self):
        input_field = input("Enter cells: ")

        game_state = [["", "", "", ""]]  # Pad field to make coordiate-to-cell mapping easy
        col = -3  # Go by column to match coordinate scheme
        while col < 0:
            new_col = [""]
            [new_col.append(x) for x in input_field[col:-10:-3]]
            game_state.append(new_col)
            col += 1

        return game_state

    def print_game_state(self):
        print("---------")
        rows = []
        row_index = 3
        while row_index > 0:
            new_row = []
            col_index = 1
            while col_index <= 3:
                new_row.append(
                    self.game_state[col_index][row_index] if self.game_state[col_index][row_index] != "_" else " ")
                col_index += 1
            rows.append(new_row)
            row_index -= 1

        for row in rows:
            print("| " + " ".join(row) + " |")
        print("---------")

    def make_human_move(self, mark):
        coordinates = input("Enter the coordinates: ").split()
        for el in coordinates:
            if not str.isdigit(el):
                print("You should enter numbers!")
                return False
        coordinates = [int(el) for el in coordinates]
        for el in coordinates:
            if not 0 < el < 4:
                print("Coordinates should be from 1 to 3!")
                return False
        col = coordinates[0]
        row = coordinates[1]
        if self.game_state[col][row] != "_":
            print("This cell is occupied! Choose another one!")
            return False
        self.game_state[coordinates[0]][coordinates[1]] = mark

    def make_computer_move(self, mark, difficulty):
        occupied = True
        while occupied:
            col = random.randint(1, 3)
            row = random.randint(1, 3)
            if self.game_state[col][row] == "_":
                self.game_state[col][row] = mark
                occupied = False
        print('Making move level "{}"'.format(difficulty))

    def game_over(self) -> bool:
        # Check if winner in col
        col = 1
        while col <= 3:
            new_col = []
            row = 1
            while row <= 3:
                new_col.append(self.game_state[col][row])
                row += 1
            if len(set(new_col)) == 1 and "_" not in new_col:
                winner = new_col[0]
                print("{} wins".format(winner))
                return True
            col += 1

        # Check if winner in row
        row = 1
        while row <= 3:
            new_row = []
            for col in range(1, 4):
                new_row.append(self.game_state[col][row])
            if len(set(new_row)) == 1 and new_row[0] != "" and "_" not in new_row:
                winner = new_row[1]
                print("{} wins".format(winner))
                return True
            row += 1

        # Check if winner in (up) diagonal
        diagonal = []
        col = 1
        row = 1
        while row <= 3:
            diagonal.append(self.game_state[col][row])
            col += 1
            row += 1
        if len(set(diagonal)) == 1 and diagonal[0] != "_":
            winner = diagonal[0]
            print("{} wins".format(winner))
            return True

        # Check if winner in (down) diagonal
        diagonal = []
        col = 1
        row = 3
        while row >= 1:
            diagonal.append(self.game_state[col][row])
            col += 1
            row -= 1
        if len(set(diagonal)) == 1 and diagonal[0] != "_":
            winner = diagonal[0]
            print("{} wins".format(winner))
            return True

        # Check for not finished
        for col in self.game_state:
            if "_" in set(col):
                return False

        # Finished, but no winner
        print("Draw")
        return True

    # def switch_player(self, player):
    #     return "X" if player == "O" else "O"

    def start_menu(self):
        stop_playing = False
        while not stop_playing:
            input_command = input("Input command: ").split()
            if len(input_command) == 1 and input_command[0] == "exit":
                stop_playing = True
                continue
            elif len(input_command) == 3 and input_command[0] == "start":
                valid_players = ["user", "easy"]
                if input_command[1] in valid_players and input_command[2] in valid_players:
                    self.play_game(input_command[1], input_command[2])
            else:
                print("Bad parameters")

    def play_game(self, player1, player2):
        self.game_state = [["", "", "", ""], ["", "_", "_", "_"], ["", "_", "_", "_"], ["", "_", "_", "_"]]
        game_over = False
        while not game_over:
            if player1 == "user":
                self.make_human_move("X")
            else:
                self.make_computer_move("X", player1)
            self.print_game_state()
            if self.game_over():
                game_over = True
                break

            if player2 == "user":
                self.make_human_move("O")
            else:
                self.make_computer_move("O", player2)
            self.print_game_state()
            if self.game_over():
                game_over = True
                break


my_game = TicTacToe
my_game()
