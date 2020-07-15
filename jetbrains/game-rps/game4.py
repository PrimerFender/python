import random

class Game:
    winning_moves = {"rock": "scissors",
                     "paper": "rock",
                     "scissors": "paper"}
    
    def __init__(self):
        self.player_name = ""
        self.player_rating = 0
        self.file_name = "rating.txt"
        self.f = open(self.file_name, "r")

    def get_player(self):
        player_name = input("Enter your name: ")
        print("Hello, {}".format(player_name))
        for lines in self.f:
            if lines.split()[0] == player_name:
                self.player_rating = int(lines.split()[1])
    
    def play(self):
        self.get_player()

        self.choice = input()
        while self.choice != "!exit":
            if self.choice == "!rating":
                print("Your rating: {}".format(self.player_rating))
            elif self.choice in self.winning_moves:
                self.computer = random.choice(["rock", "paper", "scissors"])

                if self.choice == self.computer:
                    print("There is a draw ({})".format(self.computer))
                    self.player_rating += 50
                elif Game.winning_moves[self.choice] == self.computer:
                    print("Well done. Computer chose {} and failed".format(self.computer))
                    self.player_rating += 100
                elif Game.winning_moves[self.choice] != self.computer:
                    print("Sorry, but computer chose {}".format(self.computer))
                else:
                    print("Invalid input")
            else:
                print("Invalid input")

            self.choice = input()
        print("Bye!")
        self.f.close()

my_game = Game()
my_game.play()