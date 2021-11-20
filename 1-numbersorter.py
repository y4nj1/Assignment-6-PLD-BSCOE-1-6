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
        if sec_num > third_num and third_num > fourth_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {sec_num}, {third_num}, and {fourth_num}.")
        elif sec_num < third_num and sec_num > fourth_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {third_num}, {sec_num}, and {fourth_num}.")
        elif sec_num < fourth_num and fourth_num > sec_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {third_num}, {fourth_num}, and {sec_num}.")
        elif third_num < fourth_num and third_num > sec_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {fourth_num}, {third_num}, and {sec_num}.")
        elif sec_num < fourth_num and sec_num > third_num:
            print(f"The order of the set of numbers are as follows: {first_num}, {fourth_num}, {sec_num}, and {third_num}.")
        else:
            print(f"The order of the set of numbers are as follows: {first_num}, {sec_num}, {fourth_num}, and {third_num}.")

# 3. display order
display = Order()