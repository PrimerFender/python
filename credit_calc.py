import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type of payment to calculate",
                    type=str)
parser.add_argument("--principal", help="the starting amount of credit",
                    type=int)
parser.add_argument("--periods", help="number of  times to calculate interest (usually monthly)",
                    type=int)
parser.add_argument("--interest", help="the interest rate",
                    type=float)
parser.add_argument("--payment", help="the monthly annuity payment",
                    type=int)
args = parser.parse_args()

if args.type == "diff":
    print("Differentiated")
    if args.payment is not None:
        print("Incorrect parameters")
    else:
        p = args.principal
        n = args.periods
        i = args.interest / (12 * 100)
        o = 0
        for m in range(1, n + 1):
            d = p / n + i * (p - (p * (m - 1) / n))
            d = int(math.ceil(d))
            o += d
            print("Month {}: paid out {}".format(m, d))
        o = o - p
        print("Overpayment = {}".format(o))
elif args.type == "annuity":
    print("Annuity")
    if args.interest is None:
        print("Incorrect parameters")
    else:
        a = args.payment
        p = args.principal
        n = args.periods
        i = args.interest / (12 * 100)
        o = 0
        if a is None:
            a = p * (i * (math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
            a = int(math.ceil(a))
            o = (a * n) - p
            print("Your annuity payment = {}!".format(a))
            print("Overpayment = {}".format(o))
        elif p is None:
            p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
            p = int(p)
            o = int((a * n) - p)
            print("Your credit principal = {}!".format(p))
            print("Overpayment = {}".format(o))
        elif n is None:
            n = math.log(a / (a - i * p), 1 + i)
            n = int(math.ceil(n))
            o = (a * n) - p

            years = n // 12
            months = n % 12

            message = "You need {} years ".format(years)
            if months != 0:
                message += "and {} months ".format(months)
            message += "to repay this credit!"

            print(message)
            print("Overpayment = {}".format(o))
        else:
            print("Incorrect parameters")
else:
    print("Incorrect parameters")
