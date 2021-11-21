# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# steps:
# 1. ask for 4 numbers
first_num = float(input("Enter your first number here: "))
sec_num = float(input("Enter your second number here: "))
third_num = float(input("Enter your third number here: "))
fourth_num = float(input("Enter your last number here: "))

# 2. sort from highest to lowest
highest = max(first_num, sec_num, third_num, fourth_num) # find the highest number first

def Order():
    if highest == first_num:
        if sec_num >= third_num and third_num >= fourth_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {sec_num}, {third_num}, and {fourth_num}.")
        elif sec_num <= third_num and sec_num >= fourth_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {third_num}, {sec_num}, and {fourth_num}.")
        elif sec_num <= fourth_num and fourth_num >= sec_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {third_num}, {fourth_num}, and {sec_num}.")
        elif third_num <= fourth_num and third_num >= sec_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {fourth_num}, {third_num}, and {sec_num}.")
        elif sec_num <= fourth_num and sec_num >= third_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {fourth_num}, {sec_num}, and {third_num}.")
        else:
            print(f"The order of the set of numbers are as follows: {first_num}, {sec_num}, {fourth_num}, and {third_num}.")

    if highest == sec_num:
        if first_num >= third_num and third_num >= fourth_num:
            print(f"The order of the set of numbers are as follows: {sec_num}, {first_num}, {third_num}, and {fourth_num}.")
        elif first_num >= fourth_num and fourth_num >= third_num:
            print(f"The order of the set of numbers are as follows: {sec_num}, {first_num}, {fourth_num}, and {third_num}.")
        elif first_num <= third_num and first_num >= fourth_num:
            print(f"The order of the set of numbers are as follows: {sec_num}, {third_num}, {first_num}, and {fourth_num}.")
        elif third_num >= fourth_num and fourth_num >= first_num:
            print(f"The order of the set of numbers are as follows: {sec_num}, {third_num}, {fourth_num}, and {first_num}.")
        elif first_num <= fourth_num and first_num >= third_num:
            print(f"The order of the set of numbers are as follows: {sec_num}, {fourth_num}, {first_num}, and {third_num}.")
        else:
            print(f"The order of the set of numbers are as follows: {sec_num}, {fourth_num}, {third_num}, and {first_num}.")
    
    if highest == third_num:
        if first_num >= sec_num and sec_num >= fourth_num:
            print(f"The order of the set of numbers are as follows: {third_num}, {first_num}, {sec_num}, and {fourth_num}.")
        elif first_num >= fourth_num and fourth_num >= sec_num:
            print(f"The order of the set of numbers are as follows: {third_num}, {first_num}, {fourth_num}, and {sec_num}.")
        elif first_num <= sec_num and first_num >= fourth_num:
            print(f"The order of the set of numbers are as follows: {third_num}, {sec_num}, {first_num}, and {fourth_num}.")
        elif sec_num >= fourth_num and fourth_num >= first_num:
            print(f"The order of the set of numbers are as follows: {third_num}, {sec_num}, {fourth_num}, and {first_num}.")
        elif fourth_num <= first_num and first_num >= sec_num:
            print(f"The order of the set of numbers are as follows: {third_num}, {fourth_num}, {first_num}, and {sec_num}.")
        else:
            print(f"The order of the set of numbers are as follows: {third_num}, {fourth_num}, {sec_num}, and {first_num}.")

    else:
        if highest == fourth_num:
            if first_num >= sec_num and sec_num >= third_num:
                print(f"The order of the set of numbers are as follows: {fourth_num}, {first_num}, {sec_num}, and {third_num}.")
            elif first_num >= third_num and third_num >= sec_num:
                print(f"The order of the set of numbers are as follows: {fourth_num}, {first_num}, {third_num}, and {sec_num}.")
            elif sec_num >= first_num and first_num >= third_num:
                print(f"The order of the set of numbers are as follows: {fourth_num}, {sec_num}, {first_num}, and {third_num}.")
            elif sec_num >= third_num and third_num >= first_num:
                print(f"The order of the set of numbers are as follows: {fourth_num}, {sec_num}, {third_num}, and {first_num}.")
            elif first_num <= third_num and first_num >= sec_num:
                print(f"The order of the set of numbers are as follows: {fourth_num}, {third_num}, {first_num}, and {sec_num}.")
            else:
                print(f"The order of the set of numbers are as follows: {fourth_num}, {third_num}, {sec_num}, and {first_num}.")

# 3. display order
display = Order()