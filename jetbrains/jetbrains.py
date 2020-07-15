#my_list = "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire".split(",")
my_list = ["rock", "scissors", "paper"]
user_choice = "rock"

index = 0
for option in my_list:
    if option == user_choice:
        break
    index += 1
#if index == 0:
#    ordered_list = my_list[index + 1::]
#else:
print("Index:", index)
print("Length:", len(my_list))
print("(Length - 1) / 2:", (len(my_list) - 1) / 2)
print("Length - index:", len(my_list) - index)

head_list = my_list[:index:]
tail_list = my_list[index + 1::]

if len(head_list) < (len(tail_list)):
    diff = int((len(head_list) - (len(tail_list))) / 2)
    print("Difference:", diff)
    head_list = tail_list[diff::] + head_list
    tail_list = tail_list[:diff:]

if len(head_list) > (len(tail_list)):
    diff = int((len(head_list) - (len(tail_list))) / 2)
    print("Difference:", diff)
    tail_list = tail_list + head_list[:diff]
    head_list = head_list[diff::]
    pass

print("Length:", len(head_list), "head_list:", head_list)
print("Length:", len(tail_list), "tail_list:", tail_list)
#ordered_list = head_list + tail_list

#print(ordered_list)

#print(ordered_list[:len(ordered_list) // 2])