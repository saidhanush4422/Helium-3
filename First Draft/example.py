#Example programs for research
# Get input from the user
print("Enter a number between 1 and 3:")
user_input = int(input())

# Use a switch case to perform an action based on the user's input
# The "case" clauses are used to check the value of the user's input
# The "break" statement is used to exit the switch case once a match is found
# The "default" clause is used to specify an action if the user's input does not match any of the cases

# Note: Python does not have a built-in switch case statement,
# but we can achieve a similar effect using a dictionary or a series of if-elif-else statements

# Using a dictionary

# Define the dictionary that maps input values to functions
actions = {
    1: lambda: print("You entered 1"),
    2: lambda: print("You entered 2"),
    3: lambda: print("You entered 3"),
}

# Use the dictionary to determine the action to take based on the user's input
actions.get(user_input, lambda: print("Invalid input"))()

# Using if-elif-else statements

if user_input == 1:
    print("You entered 1")
elif user_input == 2:
    print("You entered 2")
elif user_input == 3:
    print("You entered 3")
else:
    print("Invalid input")
