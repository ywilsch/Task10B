# COMPULSORY TASK 24.2 (holiday.py)
# DEFINING YOUR OWN FUNCTIONS
# 4 November 2021
# Task done by: Yolandie Wilsch

# This program will ask the user to enter information based on their holiday
# preferences. We will then use defined functions to calculate the various costs
# and present the sub-totals and grand total to the user

# Define a function that will calculate the number of days the user will
# spend in the hotel with the price per night
# Hotel_stay will be a prompt to the user, who will input an integer for the 
# calculation: the hotel_stay * 1400 per night (hotel_cost) 
def hotel_cost(hotel_stay):
    hotel_price = int(hotel_stay * 1400)
    return hotel_price

# Define a function that will request the user to input their destination of 
# of choice. Based on the destination, a price will be calculated for the flight
# Display the options of destinations to the user, asking them to "select a destination"
# flight_price is determined by the destination cost / flight (we will use a IF / ELIF statement)
def plane_cost(flight_price):
    flight_cost = flight_price *1
    return flight_cost

# Define a function the will request the user to input the number of days their will need
# to hire a car. Use a int(input( prompt to obtain the required information
# days * 350 per day to hire a car - return the total cost for the days requested
def car_rental(days):
    car_price = days * 350
    return car_price

# Define a function that will use the users input to calculate the total of the holiday
# based on the users preferences:
# Arguments: hotel_stay, flight_price and days will be required to call the previous functions
# to return a total holiday cost
# Call each function with required arguments, and add all the totals together
# Display the results neatly
def holiday_cost(hotel_stay, flight_price, days):
    total = hotel_cost(hotel_stay) + plane_cost(flight_price) + car_rental(days)
    print(f'\nThe total for your holiday is: R{total}')

# for function hotel_cost
# prompt user to enter int, asking how many nights they will stay in the hotel.
# This int value will be used to call hotel_cost() and return the hotel price / cost
hotel_stay = (int(input("How many days will you stay in the hotel? ")))

# print out a summary of the input and value of the function calculations neatly
# for the user to see as the program progresses
print(str(hotel_stay) + " days in the hotel will cost R" + str(hotel_cost(hotel_stay)))

# Display a list of destination options for the user to choose from:
print("\nFLIGHT COSTS: DESTINATION CITY")
print("Please choose your destination city:")
print("\n1. Johannesburg \n2. Cape Town \n3. Bloemfontein \n4. Kwa Zulu Natal")
    
# Ask the user to make a selection from a list of destination cities
# Based on the user input, calculate the flight price based on the destination city
destination = (int(input("\nPlease select your destination:")))

# Use an IF / ELIF statement to return the desired destination city
# Each destination city has it's own specified flight cost, this cost will be used in plane_cost()
if destination == 1:
    flight_price = 1200
    destination_name = "Johannesburg"
elif destination == 2:
    flight_price = 1600
    destination_name = "Cape Town"
elif destination == 3:
    flight_price = 950
    destination_name = "Bloemfontein"
elif destination == 4:
    flight_price = 1100
    destination_name = "Kwa Zulu Natal"
else:
    print("You have made an invalid selection.")

# Based on the users input, display a summary of the results neatly.
print("You will be arriving in " + destination_name + ". Flight price is: R" + str(plane_cost(flight_price)))

# Prompt the user to enter the number of days they will need to hire a car
# the int value will be used to call car_rental() and calculate the total car rental price
days = (int(input("\nHow many days do you need a rent-a-car? ")))

# Use the results of the function car_rental() to display a summary for the car hire costings
# display the results neatly
print("Renting a car for " + str(days) + " days at R350 per day will cost: R" + str(car_rental(days)))

# Finally, call the function holiday_cost() to calculate all the values:
# Hotel_cost() + plane_cost() + car_rental()
# Display the total cost of the holiday neatly
holiday_cost(hotel_stay, flight_price, days)