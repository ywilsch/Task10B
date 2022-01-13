# CAPSTONE PROJECT 1 - TASK 12 - (finance_calculators.py)
# 14 OCTOBER 2021
# Task done by: Yolandie Wilsch

import math

# This program will allow a user to calculate their interest on an invenstment
# or calculate the amount that should be repaid on a homeload each month

print("Choose either 'INVESTMENT' or 'BOND' from the menu below to proceed: ")
print("\nInvestment \t - to calculate the amount of interest you will earn on interest.")
print("Bond \t\t - to calculate te amount you will have to pay on a homeloan.")

# Obtain which option the user has selected, ensure that text casing will not affect the selection
opt = input("\nPlease make your selection: (Investment or Bond): ")
opt = opt.upper()

# If the user makes an invalid selection, ask them to enter a valid selection again
if opt != "INVESTMENT" and opt != "BOND" :
    print("\nYou have made an invalid selection, please try again.")
    print("\nChoose either 'INVESTMENT' or 'BOND' from the menu below to proceed: ")
    print("\nInvestment \t - to calculate the amount of interest you will earn on interest.")
    print("Bond \t\t - to calculate te amount you will have to pay on a homeloan.")

    # Ensure text casing will not cause errors
    opt = input("\nPlease make your selection: (Investment or Bond): ")
    opt = opt.upper()    

# Once user has made a valid selection, determine the deposit, rate, term and interest
if opt == "INVESTMENT" :
    deposit = float(input("\nPlease enter the amount you are going to invest: "))
    rate = float(input("Please enter the interest rate: "))
    term = int(input("Please enter the number of years you will invest your deposit: "))

    # The user can now select which type of calculation method they prefer
    interest = input("\nWould you like to calculate 'SIMPLE' or 'COMPOUND' interest rates? ")
    interest = interest.upper()

    # If the user selects simple, calculate: amount = deposit*(1 + rate * term)
    if interest == "SIMPLE" :
        amt = deposit*(1 + ((rate /100) * term))
        amt = round(amt,2)
        earned = (amt - deposit)
        earned = round(earned,2)

        # Display a summary of the input by user, with results of the calculations
        print("\n==================== RESULTS ====================")
        print("\nDeposit Amount: \t\tR " + str(deposit))
        print("Interest Rate: \t\t\t" + str(rate) + "%")
        print("Term of Investment: \t\t" + str(term) + " years")
        print("\nInterest earned: \t\tR " + str(earned))
        print("Interest Calculated on: \t" + interest)
        print("Total of Investment Return: \tR " + str(amt))
        print("\n=================================================")

    # If the user selects compound, calculate: amount = deposit * math.power((1 + rate), term)
    if interest == "COMPOUND" :
        rate = (rate / 100) # needed to generate accurate results (otherwise result is 100 times more)
        amt = deposit*math.pow((1 + rate), term)
        amt = round(amt,2)
        earned = amt - deposit
        earned = round(earned,2)
        rate = (rate*100) # to display the interest in whole numbers

        # Display a summary of the input by user, with results of the calculations
        print("\n==================== RESULTS ====================")
        print("\nDeposit Amount: \t\tR " + str(deposit))
        print("Interest Rate: \t\t\t" + str(rate) + "%")
        print("Term of Investment: \t\t" + str(term) + " years")
        print("\nInterest earned: \t\tR " + str(earned))
        print("Interest Calculated on: \t" + interest)
        print("Total of Investment Return: \tR " + str(amt))
        print("\n=================================================")

if opt == "BOND" :
    # Request the following from the user: Value of house, Annual interest rate, Number of months to repay
    print("\n============== PLEASE ENTER THE FOLLOWING DATA ==============")
    house_value = int(input("\nEnter present value of the house: "))
    # ***************************************************************************************************************************
    # NOTE TO REVIEWER: I know there is an error here - I cannot divide by 12, it causes an error, and I don't know how to fix it
    # The formula does not work, even if I use int or float or round or a combination
    # ***************************************************************************************************************************
    rate = int(input("Enter the interest rate: "))
    no_months = int(input("Enter the number of months you will repay the bond: "))

    # Formula to calculate bond repayments: repay = (i.P)/(1-(1+i)^(-n))
    repay = (rate*house_value)/(1-(1+rate)^(-no_months))
    repay = round(repay,2)

    # Print a summary of the input by the user, with results
    print("\n========================= RESULTS =========================")
    print("\nPurchase price of the house: \t\tR" + str(house_value))
    print("Interest rate: \t\t\t\t " + str(rate) + "%")
    print("No. of Months: \t\t\t\t" + str(no_months) + " months.")
    print("\nMonthly installments will be: \t\tR" + str(repay) + " per month.")
