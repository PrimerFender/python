# Espress
e_water = 250
e_beans = 16
e_cost = 4

# Latte
l_water = 350
l_milk = 75
l_beans = 20
l_cost = 7

# Cappuccino
c_water = 200
c_milk = 100
c_beans = 12
c_cost = 6

# Machine starting amount
m_money = 550
m_water = 400
m_milk = 540
m_beans = 120
m_cups = 9

def m_output():
    print("The coffee machine has:")
    print("{} of water".format(m_water))
    print("{} of milk".format(m_milk))
    print("{} of coffee beans".format(m_beans))
    print("{} of disposable cups".format(m_cups))
    print("{} of money".format(m_money))
    print()

def action_buy():
    global m_water
    global m_milk
    global m_beans
    global m_cups
    global m_money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = int(input())
    if choice == 1:
        m_water -= e_water
        m_beans -= e_beans
        m_cups -= 1
        m_money += e_cost
    elif choice == 2:
        m_water -= l_water
        m_milk -= l_milk
        m_beans -= l_beans
        m_cups -= 1
        m_money += l_cost
    elif choice == 3:
        m_water -= c_water
        m_milk -= c_milk
        m_beans -= c_beans
        m_cups -= 1
        m_money += c_cost
    else:
        print("Invalid choice")
    print()
    m_output()


def action_fill():
    global m_water
    global m_milk
    global m_beans
    global m_cups
    
    print("Write how many ml of water do you want to add:")
    m_water += int(input())
    print("Write how many ml of milk do you want to add:")
    m_milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    m_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    m_cups += int(input())

    print()
    m_output()


def action_take():
    global m_money
    
    print("I gave you ${}".format(m_money))
    m_money = 0

    print()
    m_output()


m_output()
print("Write action (buy, fill, take):")
action = input()

if action == "buy":
    action_buy()
elif action == "fill":
    action_fill()
elif action == "take":
    action_take()
else:
    print("Invalid choice")
