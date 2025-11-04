# 1. Prompt for the first number and convert input to an integer.
try:
    num1_str = input("Enter the first number:\n")
    num1 = int(num1_str)
    
    # 2. Prompt for the second number and convert input to an integer.
    num2_str = input("Enter the second number:\n")
    num2 = int(num2_str)

    # 3. Calculate the result.
    result = num1 * num2

    # 4. Display the calculation result first.
    # We use an f-string for formatted output: "42 x 42 = 1764"
    print(f"{num1} x {num2} = {result}")

    # 5. Determine and display the sign of the result using conditionals.
    if result > 0:
        # e.g., 42 x 42 = 1764 [cite: 522]
        print("The result is positive.") [cite: 523]
    elif result < 0:
        # e.g., 78 x -1 = -78 [cite: 529]
        print("The result is negative.") [cite: 530]
    else:
        # This only runs if result == 0.
        # e.g., 72 x 0 = 0 [cite: 536]
        # Note the specific required output for zero.
        print("The result is positive and negative.") [cite: 537]

except ValueError:
    # Handle cases where the user does not enter a valid integer.
    print("Error: Please enter a valid integer for both numbers.")