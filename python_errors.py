# 1:
# Correct following code - try first without running code
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print('My favorite season is', seasons[4])

# Answer: Index is not corrent. If I want to print last item from the list, I need to use index 3 or -1:
print('My favorite season is', seasons[3])
print('My favorite season is', seasons[-1])


# 2:
# Correct following code - try first without running code:

# for number in range(10):
#     # use a if the number is a multiple of 3, otherwise use b
#     if (Number % 3) == 0: # Brackets are unnecessary, variable 'Number' is supposed to be 'number'
#         message = message + a # variables 'message' and 'a' are undefined
#     else:
#         message = message + "b"
# print(message)

message = "message: "
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if number % 3 == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)


# 3:
# Ask user to type name
# ● Raise exception if name
# ○ Contains number
# ○ Has spaces
# ○ Does not start with uppercase letter
# Syntax hint: raise Exception(‘string’)

def check_name():
    name = input("Type your name: ")

    contains_digit = False
    for character in name:
        if character.isdigit():
            contains_digit = True

    if contains_digit:
        raise ValueError("Name can't contain numbers.")
    elif " " in name:
        raise ValueError("Name can't contain spaces.")
    elif name[0].islower():
        raise ValueError("Name has to start with capital letter.")
    else:
        return name

print(check_name())

# 4:
# Create function that ask user to type two integers and return division result
# ● If user type other data type than integer, ask to type
# integer
# ● If second number is 0, ask user to type number again until
# number is not 0
# ● Hint: while and/or try - except 
def numbers_division():
    while True:
        try:
            num1 = int(input("Type a number: "))
            num2 = int(input("Type another number: "))
            return num1 / num2
        except ValueError:
            print("That wasn't a number. Try it again.")
        except ZeroDivisionError:
            print("Second number can't be 0. Try it again.")

print(numbers_division())

# 5:
# Debug following code:

# year == int.input("Greetings! What is your year of origin? ')) 
# Variable is assigned with =, not ==. Int() is a function, brackets are necessary. Quotation marks have to be consistent.

# if year <= 1900 
# Double dot is necessary

#    print ('Woah, that's the past!') 
# If the string contains an apostrophe, double quotation marks have to be used.

# elif year > 1900 && year < 2020: 
# and instead of &&, <= instead of < because 2020 is present, too. This part can be siplified (without and)

#    print ("That's totally the present!")
# elif: 
# Else instead of elif.

#    print ("Far out, that's the future!!")


year = int(input("Greetings! What is your year of origin? "))
if year <= 1900:
    print("Woah, that's the past!")
elif 1900 < year <= 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")