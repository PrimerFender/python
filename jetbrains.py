import math

print("What do you want to calculate?")
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal:,')
operation = input()

if operation == "n":
    print("Enter credit principal:")
    principal = int(input())
    print("Enter monthly payment:")
    payment = int(input())
    print("Enter credit interest:")
    interest = (int(input())) / 100

    nominal_interest = interest / (12 * 100)
    periods = round(math.log(1 + nominal_interest) * (payment / ((payment - nominal_interest) * principal)))
    years = periods // 12
    months = periods % 12

    print("You need {} years and {} months to repay this credit!".format(years, months))

    # months = principal // payment
    # if principal % payment != 0:
    #    months += 1
    # months_str = str(months) + " month"
    # if months > 1:
    #    months_str += "s"
    # print()
    # print("It takes " + months_str + " to repay credit")
elif operation == "a":
    print("Enter count of months:")
    months = int(input())
    payment = principal // months
    message = "Your monthly payment = "
    if principal % months != 0:
        payment += 1
        message += str(payment)
        last_payment = principal - (months - 1) * payment
        message += " with last month payment = " + str(last_payment)
    else:
        message += str(payment)
    print()
    print(message)
elif operation == "p":
    print("Enter credit principal:")
    principal = int(input())
    print("Enter count of periods:")
    periods = int(input())
    print("Enter credit interest:")
    interest = int(input())

else:
    print("Invalid operation")
