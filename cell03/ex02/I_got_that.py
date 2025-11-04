#!/usr/bin/env python3
# Add the Shebang line above to make the script executable.

# Print the initial prompt, as shown in the example.
print("What you gotta say?")

# Start an infinite loop. We will use 'break' to exit later.
while True:
    
    # 1. Accept user input.
    user_input = input()

    # 2. Check the stop condition. The prompt specifies the exact word "STOP".
    if user_input == "STOP":
        # Exit the while loop immediately.
        break
    
    # 3. If the input is not "STOP", print the required response and continue the loop.
    # Note: The prompt is "I got that! Anything else?:"
    print("I got that! Anything else?:")