import math
import random
 
class BankingSystem:
 
    def __init__(self) -> None:
        # Card Institutional ID
 
        # [card_num, card_pin, balance
        self.accounts = []
        self.main_menu()
 
    def randomint(self, num_of_digits):
        string = ""
        for n in range(0, num_of_digits):
            string += str(random.randint(0, 9))
        return string
 
    def card_num_generator(self) -> object:
        card_iin = "400000"
        account_number = self.randomint(9)
        control_number = [int(x) for x in card_iin + account_number]
        card_num = []
        # Multiply odd digits b 2
        i = 0
        while i < len(control_number):
            control_number[i] = control_number[i] * 2
            i += 2
        # Subtract 9 to numbers over 9
        i = 0
        while i < len(control_number):
            if control_number[i] > 9:
                control_number[i] -= 9
            i += 1
        control_sum = sum([x for x in control_number])
        # Round *up* sum of modified control to nearest 10, subtract sum of control = check_sum
        check_sum = int((math.ceil(control_sum / 10.0) * 10) - control_sum)
        card_num = card_iin + str(account_number) + str(check_sum)
        return card_num
 
    def main_menu(self):
        ready_to_quit = False
        while not ready_to_quit:
            print("1. Create an account")
            print("2. Login into account")
            print("0. Exit")
            choice = input()
            print()
 
            if choice == "1":
                self.account_create()
            elif choice == "2":
                self.account_login()
            elif choice == "0":
                self.quit_program()
            else:
                print("Invalid input")
 
 
    def account_create(self):
        # Generate Card & Pin & Checksum
        card_num = self.card_num_generator()
        card_pin = self.randomint(4)
        # Add account to system
        balance = 0
        self.accounts.append([card_num, card_pin, balance])
        print("Your card number:")
        print(card_num)
        print("Your card PIN:")
        print(card_pin)
        print()
 
    def account_login(self):
        account = []
 
        # authenticated = False
        # while not authenticated:
        print("Enter your card number:")
        card_num = input()
        print("Enter your PIN:")
        card_pin = input()
        print()
 
        for acct in self.accounts:
            if acct[0] == card_num:
                account = acct
                break
 
        if len(account) != 0 and account[1] == card_pin:
            # authenticated = True
            print("You have successfully logged in!")
            print()
            self.acccount_menu(account)
        else:
            print("Wrong card number or PIN!")
            print()
 
    def acccount_menu(self, account):
        wanting_to_leave = False
 
        while not wanting_to_leave:
            print("1. Balance")
            print("2. Log out")
            print("0. Exit")
            choice = input()
            print()
 
            if choice == "1":
                print("Balance: {}".format(account[2]))
                print()
            elif choice == "2":
                print("You have successfully logged out!")
                print()
                self.main_menu()
            elif choice == "0":
                self.quit_program()
            else:
                print("Invalid Input")
                print()
 
    def quit_program(self):
        print("Bye!")
        exit()
 
 
my_bank = BankingSystem()
my_bank