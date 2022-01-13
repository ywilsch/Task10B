# COMPULSORY TASK 24.1 (my_function.py)
# DEFINING YOUR OWN FUNCTIONS
# 4 November 2021
# Task done by: Yolandie Wilsch

# PART ONE
# Create a function that prints out all the days of the week
# Define a function that will contain the list of all the days of the week
# When the user needs to print the days, they can recall the function
def days_of_week():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print([days])    

# PART TWO
# Create a program that takes in a string input from a user and replaces every second word with 'hello'
# Create a function that will evaluate the string:
def insert(sentence):
    # Use the split function to extract each word entered in the string, and store it into a list
    i = sentence.split(" ")
    
    # Evaluate the list, and identify each odd index entry, starting at position 0
    # Create an empty list which will store the evaluated values
    odd_word = i[0::2]
    print(odd_word)
    list = []
    
    # For each odd word (indexed result), replace that word with the new value 'hello'
    for word in odd_word:
        list.append(word)
        list.append("hello")
    
    # Create a new string, which contains the inserted 'hello' words each odd index position
    # Join the words together, into the empty list
    last_string = " ".join(list)
    
    # Print the final result
    print(last_string)

# Create a string using INPUT, and ask the user to enter any sentence which will be 
# evaluated by the function INSERT
# Call the function, INSERT, and display the final result
string = insert(input("Please enter a sentence: "))
print(string)
