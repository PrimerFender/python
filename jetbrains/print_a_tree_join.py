height = int(input())

def get_total():
    width = 1
    for _ in range(1, height):
        width += 2
    return width

count = 1
for _ in range(0, height):
    output = ("#" * count).center(get_total())
    count += 2
    print(output)
