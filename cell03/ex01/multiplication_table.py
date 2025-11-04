#!/usr/bin/env python3
# Add the Shebang line above to make the script executable.

# 1. Prompt for input as required by the example.
print("Enter a number")

try:
    # 2. Get user input and convert it to an integer.
    number_str = input()
    number = int(number_str)

    # 3. Use a for loop to iterate from 0 to 9 (range(10) includes 0 but excludes 10).
    for i in range(10):
        # Calculate the product
        result = i * number
        
        # 4. Print the formatted equation: "i x number = result"
        # We use an f-string to easily insert variables into the output string.
        print(f"{i} x {number} = {result}")

except ValueError:
    # Handle non-integer input gracefully
    print("Error: Invalid input. Please enter a valid integer.")