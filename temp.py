class Game:
    def __init__(self):
        self.game_state = "Eat"

class Player(Game):
    def __init__(self):
        self.name = "Player1"

class ComputerPlayer(Player):
    def __init__(self):
        self.difficulty = "Easy"

new_game = Game()
new_player = ComputerPlayer()
print(new_player.difficulty)
print(new_player.name)
