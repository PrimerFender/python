ml_water = 200
ml_milk = 50
g_beans = 15
print("Write how many cups of coffee you will need:")
qty_cups = int(input())
print("For 125 cups of coffee you will need:")
print("{} ml of water".format(qty_cups * ml_water))
print("{} ml of milk".format(qty_cups * ml_milk))
print("{} ml of beans".format(qty_cups * g_beans))