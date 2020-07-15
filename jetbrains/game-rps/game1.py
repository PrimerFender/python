import random

class Game:
    winning_moves = {"rock": "scissors",
                     "paper": "rock",
                     "scissors": "paper"}

    def play(self):
        self.choice = input()

        while self.choice != "!exit":
            if self.choice in self.winning_moves:
                self.computer = random.choice(["rock", "paper", "scissors"])

                if self.choice == self.computer:
                    print("There is a draw ({})".format(self.computer))
                elif Game.winning_moves[self.choice] == self.computer:
                    print("Well done. Computer chose {} and failed".format(self.computer))
                elif Game.winning_moves[self.choice] != self.computer:
                    print("Sorry, but computer chose {}".format(self.computer))
                else:
                    print("Invalid input")
            else: print("Invalid input")

            self.choice = input()
        print("Bye!")


my_game = Game()
my_game.play()