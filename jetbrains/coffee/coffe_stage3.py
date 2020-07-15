ml_water = 200
ml_milk = 50
g_beans = 15

print("Write how many ml of water the coffee machine has:")
in_water = int(input())
print("Write how many ml of milk the coffee machine has:")
in_milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
in_beans = int(input())
print("Write how many cups of coffee you will need:")
in_cups = int(input())

cups_water = in_water // ml_water
cups_milk = in_milk // ml_milk
cups_beans = in_beans // g_beans

max_cups = min([cups_water, cups_milk, cups_beans])

if max_cups < in_cups:
    print("No, I can only make {} cups of coffee".format(max_cups))
elif max_cups == in_cups:
    print("Yes, I can make that amount of coffee")
else:
    print("Yes, I can make that amount of coffee (even {} more than that)".format(max_cups - in_cups))