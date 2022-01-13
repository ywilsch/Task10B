# COMPULSORY TASK 24.3 (amazon.py)
# DEFINING YOUR OWN FUNCTIONS
# 9 November 2021
# Task done by: Yolandie Wilsch

# Define a function that will calculate the MIN value in the list of numbers
# Open / write to the file 'output.txt' to add the values in the text file
# The printing line of code was purely for screen viewing, and not necessary,
# but helpful when checking and debugging
def calc_min(numbers):
    min_no = min(numbers)
    file = open('output.txt', 'a+')
    file.writelines(f'The MIN of {numbers} is {min_no}\n')
    file.close()
    print('The min of ', (numbers), ' is ', min(numbers))

# Define a function that will return the MAX value in the list of numbers
# Again, write the values to 'output.txt'
# Values of this function must be added to the current file, not overwrite MIN values
def calc_max(numbers):
    max_no = max(numbers)
    file = open('output.txt', 'a+')
    file.writelines(f'The MAX of {numbers} is {max_no}\n')
    file.close()
    print('The max of ', (numbers), ' is ', max(numbers))

# Define a function that will return the AVERAGE value of the list of numbers
# Write the values to 'output.txt' on a new line
def calc_avg():
    avg_no = sum(numbers)/len(numbers)
    file = open('output.txt', 'a+')
    file.writelines(f'The AVERAGE of {numbers} is {avg_no}\n')
    file.close()
    print('The average of', (numbers), ' is ', sum(numbers)/len(numbers))

# For each line of input (input.txt) write a new line in output.txt
# Read the file 'input.txt'
# For other methods, the file needs to be encoded=utf-8-sig to remove the \ufeff
# However, for this method, it is not necessary
with open('input.txt','r') as my_file:
    for line in my_file:
        # Strip each line by the : to remove the min, max, avg
        lines = line.strip().split(':')
        # Split the remainder of the values using the ',' creating a list of numbers
        # which will be used for all calculations
        numbers = [int(x) for x in lines[1].split(',')]

# Display results on the screen - for checking / debugging purposes only
calc_min(numbers)
calc_max(numbers)
calc_avg()
