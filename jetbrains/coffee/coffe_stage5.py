# Supply names = ["water", "milk", "beans", "cost", "cups", "money"]
supply_names = ["water", "milk", "cofee beans", "disposable cups", "money"]

# Machine Supplies = [water, milk, beans, cost, cups, money]
machine_supplies = [400, 540, 120, 9, 550]

# Coffee supplies = [water, milk, beans, cups, cost]
espresso_supplies = [-250, -0, -16, -1, 4]
latte_supplies = [-350, -75, -20, -1, 7]
cappuccino_supplies = [-200, -100, -12, -1, 6]

# List of coffees
coffee_list = [espresso_supplies, latte_supplies, cappuccino_supplies]


def m_output():
    print("The coffee machine has:")

    index = 0
    for supply in machine_supplies:
        print("{} of {}".format(supply, supply_names[index]))
        index += 1
    print()

def check_supplies(coffee_supplies):
    global machine_supplies
    # Check if enough
    index = 0
    for supply in coffee_supplies:
        if machine_supplies[index] + supply <= 0:
            print("Sorry not enough {}!".format(supply_names[index]))
            print()
            return
        index += 1
    
    # Update machine
    print("I have enough resources, making you a coffee!")
    print()
    index = 0
    for supply in coffee_supplies:
        machine_supplies[index] += supply
        index += 1

def action_buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:")
    choice = input()
    if choice == "back":
        return
    
    choice = int(choice)
    check_supplies(coffee_list[choice - 1])

def action_fill():
    global machine_supplies
    
    print("Write how many ml of water do you want to add:")
    machine_supplies[0] += int(input())
    print("Write how many ml of milk do you want to add:")
    machine_supplies[1] += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    machine_supplies[2] += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    machine_supplies[3] += int(input())
    print()


def action_take():
    global machine_supplies
    
    print("I gave you ${}".format(machine_supplies[4]))
    machine_supplies[4] = 0
    print()


action = ""
while action != "exit":
    print("Write action (buy, fill, take), remaining, exit:")
    action = input()
    print()

    if action == "buy":
        action_buy()
    elif action == "fill":
        action_fill()
    elif action == "take":
        action_take()
    elif action == "remaining":
        m_output()
    elif action == "exit":
        break
    else:
        print("Invalid choice")
