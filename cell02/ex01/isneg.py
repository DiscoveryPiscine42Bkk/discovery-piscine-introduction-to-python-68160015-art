try:
    number_str = input()
    number = int(number_str)

    if number < 0: 
        print("This number is negative.")

    elif number == 0: 
       
        print("This number is both positive and negative.")

    else:
        print("This number is positive.")

except ValueError:
    print("Error: Please enter a valid integer.")