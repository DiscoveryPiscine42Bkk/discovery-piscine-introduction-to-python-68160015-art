try:
    number_str = input()
    number = int(number_str)


    if number == 0:
        print("This number is equal to zero.")
    else: 
        print("This number is different from zero.")
except ValueError:
  
    print("Invalid input: Please enter an integer.")