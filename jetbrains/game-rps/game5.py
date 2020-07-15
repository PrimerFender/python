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
        self.winners_list = []
        self.losers_list = []
        self.computer = ""

    def get_player(self):
        player_name = input("Enter your name: ")
        print("Hello, {}".format(player_name))
        for lines in self.f:
            if lines.split()[0] == player_name:
                self.player_rating = int(lines.split()[1])
    
    def get_options(self, options="rock,paper,scissors"):
        print("Okay, let's start")
        options_list = options.split(",")
        index = 0
        for option in options_list:
            if index % 2 != 0:
                self.winners_list.append(option)
            else:
                self.losers_list.append(option)
            index += 1
    
    def get_computer(self):
        my_list = random.randint(0, 1)
        return random.choice(self.winners_list) if my_list == 0 else random.choice(self.losers_list)
    
    def play(self):
        self.get_player()
        options = input()
        if options == "":
            print("OK, let's get start")
            self.choice = input()
            while self.choice != "!exit":
                if self.choice == "!rating":
                    print("Your rating: {}".format(self.player_rating))
                    self.choice = input()
                    continue
                elif self.choice in self.winning_moves:
                    self.computer = random.choice(["rock", "paper", "scissors"])
                else:
                    print("Invalid input")
                    self.choice = input()
                    continue

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
                self.choice = input()
        else:
            self.get_options(options)
            self.choice = input()
            while self.choice != "!exit":
                if self.choice == "!rating":
                    print("Your rating: {}".format(self.player_rating))
                    self.choice = input()
                    continue
                else:
                    self.computer = self.get_computer()

                if self.choice == self.computer:
                    print("There is a draw ({})".format(self.computer))
                    self.player_rating += 50
                elif self.choice in self.winners_list:
                    print("Well done. Computer chose {} and failed".format(self.computer))
                    self.player_rating += 100
                elif self.choice in self.losers_list:
                    print("Sorry, but computer chose {}".format(self.computer))
                else:
                    print("Invalid input")

            self.choice = input()
        print("Bye!")
        self.f.close()

my_game = Game()
my_game.play()