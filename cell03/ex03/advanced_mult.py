#!/usr/bin/env python3
# Add the Shebang line above to make the script executable.

import sys

# Check the number of arguments provided (including the script name).
# If len(sys.argv) > 1, it means the user provided extra arguments.
if len(sys.argv) > 1:
    # If any argument is present, display the required error message.
    print("none")
    
else:
    # If no extra arguments are present, generate the multiplication tables (0 to 10).
    
    # Outer loop: Iterates through the table number (N) from 0 to 10.
    for table_num in range(11): # range(11) gives numbers 0, 1, 2, ..., 10
        
        # Start the line with the required prefix.
        output_line = f"Table de {table_num}:"
        
        # Inner loop: Iterates through the multiplier (i) from 0 to 10.
        for i in range(11):
            result = table_num * i
            # Append the result to the line with a space separator.
            output_line += f" {result}"
            
        # Print the complete line for the current table.
        print(output_line)