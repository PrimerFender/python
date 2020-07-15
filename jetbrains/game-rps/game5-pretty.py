# Write your code here
import random
import math


def game_winner(choice, options):
    ind = options.index(choice)
    options = options[ind+1:] + options[:ind]
    return options[:math.floor(len(options)/2)]


choices = ['rock', 'paper', 'scissors']
rating = 0
user_name = input('Enter your name:')
print("Hello", user_name)

with open('rating.txt', 'r') as rating_file:
    for line in rating_file:
        player_rating = line.split()
        if player_rating[0] == user_name:
            rating = player_rating[1]

user_choices = input().split(',')
if user_choices != ['']:
    choices = user_choices

print("Okay, let's start")
while True:
    user_selection = input()
    computer_choice = random.choice(choices)
    if user_selection == "!exit":
        print("Bye!")
        break
    elif user_selection == "!rating":
        print("Your rating:", rating)
        continue
    elif user_selection not in choices:
        print("Invalid input")
        continue
    elif user_selection == computer_choice:
        print(f"There is a draw ({computer_choice})")
        rating += 50
    elif user_selection in game_winner(computer_choice, choices):
        print(f"Well done. Computer chose {computer_choice} and failed")
        rating += 100
    else:
        print("Sorry, but computer chose", computer_choice)
