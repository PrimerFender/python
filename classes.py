from random import randint


class Game:
    game_state = [0, 1, 3]

    def __init__(self):
        print("Game", self.game_state)

    def update_state(self, offset):
        self.game_state = [randint(0, 9) + offset, randint(0, 9) - offset, randint(0, 9) * offset]


class Player(Game):
    def __init__(self, mark):
        self.mark = mark

    def update_state(self, game, offset):
        game.game_state = [randint(0, 9) + offset, randint(0, 9) - offset, randint(0, 9) * offset]


game_1 = Game()
player_1 = Player("X")
player_2 = Player("O")

player_1.update_state(game_1, 69)
print("Player1: ", game_1.game_state)
player_2.update_state(game_1, 420)
print("Player2: ", game_1.game_state)

print("Game1: ", game_1.game_state)
