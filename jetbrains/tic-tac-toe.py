class TicTacToe:

    def __init__(self):
        self.game_state = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.players = ["X", "O"]
        self.draw_field()
        self.play_game()

    def play_game(self):
        game_over = False
        while not game_over:
            move = input("Enter the coordinates: ")
            if len(move) != 3 or " " not in move:
                print("You should enter numbers!")
                continue
            else:
                move = move.split()
            move_x = int(move[0])
            move_y = int(move[1])
            if move_x < 1 or move_x > 3 or move_y < 1 or move_y > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            else:
                translate_y = [2, 1, 0]
                move_x = int(move[0]) - 1
                move_y = translate_y[int(move[1]) - 1]
            if self.game_state[move_y][move_x] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                self.game_state[move_y][move_x] = self.players[0]
                self.players.reverse()
                self.draw_field()
                game_over = self.check_game_state()

    def draw_field(self):
        empty_row = list("| _ _ _ |")
        first_row = [x for x in empty_row]
        second_row = [x for x in empty_row]
        third_row = [x for x in empty_row]

        first_row[2] = self.game_state[0][0]
        first_row[4] = self.game_state[0][1]
        first_row[6] = self.game_state[0][2]

        second_row[2] = self.game_state[1][0]
        second_row[4] = self.game_state[1][1]
        second_row[6] = self.game_state[1][2]

        third_row[2] = self.game_state[2][0]
        third_row[4] = self.game_state[2][1]
        third_row[6] = self.game_state[2][2]

        row_outside = "---------"
        print(row_outside)
        print(''.join(first_row))
        print(''.join(second_row))
        print(''.join(third_row))
        print(row_outside)

    def check_game_state(self) -> bool:
        # Check for win
        # Check rows
        wins = 0
        winner = ""
        for row in self.game_state:
            if len(set(row)) == 1 and "_" not in set(row):
                wins += 1
                winner = row[0]
        #all([x in row for row in self.game_state])
        if wins == 1:
            print("{} wins".format(winner))
            return True
        if wins > 1:
            print("Impossible")
            return False

        # Check columns
        wins = 0
        winner = ""
        columns = []
        for column in range(3):
            columns.append([x[column] for x in self.game_state])
        for column in columns:
            if len(set(column)) == 1 and "_" not in set(row):
                wins += 1
                winner = column[0]
        if wins == 1:
            print("{} wins".format(winner))
            return True
        if wins > 1:
            print("Impossible")
            return False

        # Check diagonals
        down_right = []
        up_right = []
        for i in range(3):
            down_right.append(self.game_state[i][i])
        if len(set(down_right)) == 1 and "_" not in set(row):
            print("{} wins".format(down_right[0]))
            return True
        j = 0
        for i in range(2, -1, -1):
            up_right.append(self.game_state[i][j])
            j += 1
        if len(set(up_right)) == 1 and "_" not in set(row):
            print("{} wins".format(up_right[0]))
            return True

        # Check draw
        is_draw = True
        for row in self.game_state:
            if "_" in set(row):
                is_draw = False
        if is_draw:
            print("Draw")
            return True

        # Check impossible (too many)
        # num_x = 0
        # num_o = 0
        # for row in self.game_state:
        #     for cell in row:
        #         if cell == "X":
        #             num_x += 1
        #         if cell == "O":
        #             num_o += 1
        # if (abs(num_x - num_o)) > 1:
        #     print("Impossible")
        #     return True

        # Check not finished
        # is_finished = True
        # for row in self.game_state:
        #     if "_" in set(row):
        #         is_finished = False
        # if not is_finished:
        #     print("Game not finished")


my_game = TicTacToe()
