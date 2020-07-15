import random
from string import ascii_lowercase

class Hangman:

    word_list = ("python", "java", "kotlin", "javascript")

    def __init__(self):
        self.input_str = ""

        self.game_menu()
    
    def game_menu(self):
        print("H A N G M A N")
        
        menu = 'Type "play" to play the game, "exit" to quit: '
        self.input_str = input(menu)
        while self.input_str != "exit":
            if self.input_str != "play":
                self.input_str = input(menu)
                continue
            else:
                self.guess_the_word(random.choice(Hangman.word_list))

    def salutation(self, win, word=""):
        if win:
            print("You guessed the word {}!".format(word))
            print("You survived!")
        else:
            print("You are hanged!")
            print()
    
    def display_word(self, word, guesses):
        word_display = ""
        for char in word:
            if char in guesses:
                word_display += char
            else:
                word_display += "-"
        return word_display

    def validate_input(self, input_str):
        if len(input_str) > 1:
            print("You should input a single letter")
            return False
        if input_str not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            return False

        return True

    def guess_the_word(self, word):
        lives_remaining = 8
        guessed_letters = set()

        while lives_remaining > 0:
            print()
            print(self.display_word(word, guessed_letters))

            self.input_str = input("Input a letter: ")
            if self.input_str == "exit":
                return

            if self.validate_input(self.input_str):
                if self.input_str in guessed_letters:
                    print("You already typed this letter")
                    continue
                
                guessed_letters.add(self.input_str)
                if guessed_letters == set(word):
                    self.salutation(True)
                    break
                elif self.input_str not in word:
                    lives_remaining -= 1
                    print("No such letter in the word")
        else:
            self.salutation(False)

my_game = Hangman()