# 1. Define the correct password variable.
CORRECT_PASSWORD = "Python is awesome"

# 2. Prompt the user for a password and store the input[cite: 575].
# Note: The input function does not automatically display a prompt, it just waits for input.
user_input = input()

# 3. Use a conditional statement to check if the input matches the correct password[cite: 576].
if user_input == CORRECT_PASSWORD:
    # If the password is correct, display "ACCESS GRANTED"[cite: 576].
    print("ACCESS GRANTED")
else:
    # Otherwise, display "ACCESS DENIED."[cite: 576].
    print("ACCESS DENIED")