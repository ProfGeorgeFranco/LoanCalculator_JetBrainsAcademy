# write your code here
import math

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type")

parser.add_argument("--principal")

parser.add_argument("--payment")

parser.add_argument("--periods")

parser.add_argument("--interest")

args = parser.parse_args()

#  ******************* User input arguments verification *******************

if str(args.principal) != "None":
    user_principal = float(args.principal)
    if user_principal <= 0:
        print("Incorrect parameters. principal")
        exit()

if str(args.payment) != "None":
    user_payment = float(args.payment)
    if user_payment <= 0:
        print("Incorrect parameters.")
        exit()

if str(args.periods) != "None":
    user_periods = int(args.periods)
    if user_periods <= 0:
        print("Incorrect parameters.")
        exit()

if str(args.interest) != "None":
    user_interest = float(args.interest) / 1200
    if user_interest <= 0:
        print("Incorrect parameters.")
        exit()

if str(args.interest) == "None":
    print("Incorrect parameters.")
    exit(0)


#  *******************  Functions  *******************
def annuity_function():

    #  Monthly payments calculation
    if str(args.principal) != "None" and str(args.periods) != "None" and str(args.payment) == "None":
        monthly_pay = user_principal * (user_interest * math.pow(1 + user_interest, user_periods)) / (
                    math.pow(1 + user_interest, user_periods) - 1)
        print(f"Your annuity payment = {math.ceil(monthly_pay)}!")
        print(f"Overpayment {math.ceil(math.ceil(monthly_pay) * user_periods - user_principal)}")

    #  Loan Principal calculation
    elif str(args.periods) != "None" and str(args.payment) != "None" and str(args.principal) == "None":
        principal = user_payment / (
                (user_interest * math.pow(1 + user_interest, user_periods)) / (
                math.pow(1 + user_interest, user_periods) - 1))

        print(f"Your loan principal = {math.floor(principal)}!")
        print(f"Overpayment = {int(user_payment * user_periods - math.floor(principal))}")

    #  Period calculation
    elif str(args.principal) != "None" and str(args.periods) == "None" and str(args.payment) != "None":
        total_month = (math.ceil(math.log(user_payment / (user_payment - user_interest * user_principal), 1 + user_interest)))

        total_year = total_month // 12

        extra_month = total_month % 12

        if total_year == 0:
            if extra_month == 1:
                print(f"It will take {extra_month} month to repay the loan!")
                print(f"Overpayment = {user_payment * total_month - user_principal}")
            elif extra_month > 1:
                print(f"It will take {extra_month} months to repay the loan!")
                print(f"Overpayment = {user_payment * total_month - user_principal}")

        elif total_year == 1:
            if extra_month == 0:
                print(f"It will take {total_year} year to repay the loan!")
                print(f"Overpayment = {user_payment * total_month - user_principal}")

            elif extra_month == 1:
                print(f"It will take {total_year} year and {extra_month} month to repay the loan!")
                print(f"Overpayment = {user_payment * total_month - user_principal}")

            else:
                print(f"It will take {total_year} year and {extra_month} months to repay the loan!")
                print(f"Overpayment = {user_payment * total_month - user_principal}")


        elif total_year > 1:
            if extra_month == 0:
                print(f"It will take {total_year} years to repay the loan!")
                print(f"Overpayment = {user_payment * total_month - user_principal}")

            elif extra_month == 1:
                print(f"It will take {total_year} years and {extra_month} month to repay the loan!")
                print(f"Overpayment = {user_payment * total_month - user_principal}")

            else:
                print(f"It will take {total_year} years and {extra_month} months to repay the loan!")
                print(f"Overpayment = {user_payment * total_month - user_principal}")

    return


def diff_function():
    if str(args.principal) == "None" or str(args.periods) == "None":
        print("Incorrect parameters.")
        return

    diff_payment = 0

    for x in range(1, user_periods + 1):
        month_pay = user_principal / user_periods + user_interest * (
                user_principal - (user_principal * (x - 1)) / user_periods)
        print(f"Month {x}: payment is {math.ceil(month_pay)}")
        diff_payment += math.ceil(month_pay)

    print(f"\nOverpayment = {math.ceil(diff_payment - user_principal)}")
    return


#  ******************* Main script *******************

if args.type == "annuity":
    annuity_function()

elif str(args.type) == "diff":
    diff_function()

else:
    print("Incorrect parameters fim.")
