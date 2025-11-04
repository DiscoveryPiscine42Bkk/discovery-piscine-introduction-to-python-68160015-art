
# The program prompts for a number.
print("Enter a number less than 25") 

try:
    # Get user input and convert it to an integer.
    number_str = input()
    number = int(number_str)
    
    # Check the initial condition: Is the number greater than 25?
    if number > 25:
        print("Error") # Display "Error" if greater than 25. [cite: 1346, 1347]
    else:
        # Use a while loop as instructed  to count up to 25.
        # The loop continues as long as the current number is less than or equal to 25.
        while number <= 25:
            # Display the required message and the current number.
            print(f"Inside the loop, my variable is {number}")
            # Increment the number to move to the next value.
            number += 1 

except ValueError:
    # Handle cases where the input is not a valid integer.
    print("Error: Invalid input (Not a number).")