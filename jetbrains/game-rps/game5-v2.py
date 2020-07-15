import random

class Game:
    winning_moves_ref = {"rock": "scissors",
                         "scissors": "paper",
                         "paper": "rock"}
    

    def __init__(self):
        self.file_name = "rating.txt"
        self.f = open(self.file_name, "r")
        self.player_name = ""
        self.player_rating = 0
        self.options_list = []
        self.winners_list = []
        self.losers_list = []

    def get_player(self):
        player_name = input("Enter your name: ")
        print("Hello, {}".format(player_name))
        for lines in self.f:
            if lines.split()[0] == player_name:
                self.player_rating = int(lines.split()[1])
    
    def set_game_options(self, options="rock,paper,scissors"):
        print("Okay, let's start")
        self.options_list = options.split(",")
    
    def get_options(self, options="rock,paper,scissors"):
        options_list = options.split(",")
        index = 0
        for option in options_list:
            if index % 2 != 0:
                self.winners_list.append(option)
            else:
                self.losers_list.append(option)
            index += 1
        print("Okay, let's start")
    
    def get_computer(self):
        my_list = random.randint(0, 1)
        return random.choice(self.winners_list) if my_list == 0 else random.choice(self.losers_list)
    
    def play(self):
        self.get_player()
        options = input()
        if options == "":
            use_default_options()
        elif options != "":
            set_custom_options(options)
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

    def new_play(self, user_input):
        while user_input != "!exit":
            if user_input == "!rating":
                print("Your rating: {}".format(self.player_rating))
            # Check player input is for choice in game
            elif user_input in self.options_list:
                # Computer choice
                user_choice = user_input
                computer_choice = random.choice(self.options_list)
                if  user_choice == computer_choice:
                    print("There is a draw ({})".format(computer_choice))
                    self.player_rating += 50
                else:
                    index = 0
                    for option in self.options_list:
                        if option == user_choice:
                            break
                        index += 1
                    head_list = self.options_list[:index:]
                    tail_list = self.options_list[index + 1::]

                    if len(head_list) < (len(tail_list)):
                        diff = int((len(head_list) - (len(tail_list))) / 2)
                        head_list = tail_list[diff::] + head_list
                        tail_list = tail_list[:diff:]

                    if len(head_list) > (len(tail_list)):
                        diff = int((len(head_list) - (len(tail_list))) / 2)
                        tail_list = tail_list + head_list[:diff]
                        head_list = head_list[diff::]

                    #ordered_list = head_list + tail_list
                    if computer_choice in tail_list:
                        print("Sorry, but computer chose {}".format(computer_choice))
                    else:
                        print("Well done. Computer chose {} and failed".format(computer_choice))
                        self.player_rating += 100
            else:
                print("Invalid input")
            # Continue playing
            user_input = input()

# Create the game
my_game = Game()

# Introduce the game
my_game.get_player()

# Chose game style
options = input()
if options == "":
    my_game.set_game_options()
else:
    my_game.set_game_options(options)

# Start the game
my_game.new_play(input())