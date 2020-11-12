# 1:
# Create function to divide first number by the second number (numbers are parameters)
def division(num1, num2):
    return num1 / num2

print(division(30, 4)) # 7.5

print()


# 2:
# Create function that has list of numbers as an input and prints sum of all elements of the list
def addition(num_list):
    return sum(num_list)

print(addition(list(range(10)))) # 45

print()


# 3:
# Using lambda create function that
# ○ Takes a list as an input
# ○ If list length is more than 5, prints 'big list'
# ○ Else it prints 'small list'

compare_list = lambda a : "big list" if len(a) > 5 else "small list"
print(compare_list([1, 2, 3, 4, 5, 6])) # big list
print(compare_list([1, 2, 3])) # small list

print()


# 4:
# Write function that has one parameter (string) and returns
# ○ String
# ○ Number of uppercase letters
# ○ Number of lowercase letters

def string_upper_lower(text):
    up_count = 0
    low_count = 0
    for character in text:
        if character.isupper():
            up_count += 1
        elif character.islower():
            low_count += 1
    statement = "{}\nUppercase letters: {}\nLowercase letters: {}\n".format(text, up_count, low_count)
    return statement

text = "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers, where’s the peck of pickled peppers Peter Piper picked?"
print(string_upper_lower(text))
# Uppercase letters: 10
# Lowercase letters: 148

print()


# 5:
# Create a function with two parameters:
# ○ Lunch cost
# ○ Meal voucher value
# Function will compute how much to pay in meal vouchers and how much remains to be paid in cash

def meal_vouchers(lunch_price, voucher_value):
    vouchers_needed = lunch_price // voucher_value
    cash_needed = lunch_price - voucher_value * vouchers_needed
    statement = "Lunch price: {} CZK\nPay in cash: {} CZK\nPay in meal vouchers: {} pcs, {} CZK each".format(lunch_price, cash_needed, vouchers_needed, voucher_value)
    return statement


print(meal_vouchers(500, 74))
# Lunch price: 500 CZK
# Pay in cash: 56 CZK
# Pay in meal vouchers: 6 pcs, 74 CZK each

print()


# 6: Using recursion, write function that computes factorial for positive integer

def compute_factorial(num):
    if num < 0:
        return None
    elif num <= 1:
        return 1
    else:
        return num * compute_factorial(num - 1)

print(compute_factorial(1)) # 1
print(compute_factorial(3)) # 6
