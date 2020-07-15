string = "15325"
#string = "123"
num_list = [int(x) for x in string]

print(num_list)
running_total = []

index = 0
for x in num_list:
    if index == 0:
        running_total.append(x)
    else:
        running_total.append(running_total[index - 1] + x)
    index += 1
print(running_total)

# Get user input of numbers
user_input = input()
# Transform str numbers to int numbers
nums = [int(x) for x in user_input]

run_total = [sum(nums[:x + 1]) for x in range(len(nums))]
'''
the above code is the same as:

run_total = []
for x in range(len(nums)):
    run_total.append(sum(nums[:x + 1]))

What this does is sum the numbers from the list nums starting at index 0 up to index x + 1 on each pass.
So say len(nums) == 3, the code will execute like this:
sum all the numbers from index 0 to index 1 (x + 1 where x starts at 0) and append to run_total
sum all the numbers from index 0 to index 2 (x + 1 where x is now 1) and append to run_total
sum all the numbers from index 0 to index 3 (x + 1 where x in now 2) and append to run_total.
X is now 3 and exits the for loop.
'''
print(run_total)  # print the running total list
