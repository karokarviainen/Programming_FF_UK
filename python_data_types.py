# 1:
# The king with lots of children got heritage - 1256983
# golden coins. He decided that he will divide his heritage
# evenly among all of his 28 children. How many coins will
# remain to him? 
kings_coins = 1256983 % 28
print(kings_coins) # 7 coins


# 2:
# Evaluate if following is true
#   ○ Remainder after division of 12**52 by 15 is less than 8 or 3**5 is more than 100
print(12 ** 52 % 15 < 8 or 3 ** 5 > 100) # True

#   ○ 5 times 3**3 is not equal to 900 divided by 75
print(5 * 3 ** 3 != 900 / 75) # True


#3:
# Create one string from the 2 following strings:
#   ○ '[[]]' + 'PYTHON ' → '[[PYTHON]]'
str1, str2 = '[[]]', 'PYTHON'
print(str1[:2] + str2 + str1[2:]) # '[[PYTHON]]'

# Create one string from another
#   ○ 'Python' → 'onononon'
#   ○ 'Perl' → 'rrrrrr'
str1 = 'Python'
print(str1[-2:] * 4) # 'onononon'
str2 = 'Perl'
print(str2[2] * 6) # 'rrrrrr'


#4:
# Make first half of the string uppercase and second half lowercase
# ○ E.g. 'python' ---> 'PYThon'
str1 = 'python'
print(str1[:3].upper() + str1[3:]) # 'PYThon'

# Create string which is first letter of another string repeated n
# number of times, where n - length of the given string
# ○ E.g. 'python' ---> 'pppppp'
# ○ 'git' ---> 'ggg'
str1, str2 = 'python', 'git'
print(str1[0] * len(str1)) # 'pppppp'
print(str2[0] * len(str2)) # 'ggg'


# 5:
# What results do you get when you run following expressions?
# ○ print(7+3*2)
print(7+3*2) # 13 - Multiplication and addition works normally

# ○ print('7' + str(3*2))
print('7' + str(3*2)) # '76' - two strings '7' and '6' are added together

# ○ print('7' + '3*2')
print('7' + '3*2') # '73*2' - two strings '7' and '3*2' are added together

# ○ print('7' + 3*2)
# What is causing error ?
#print('7' + 3*2) # TypeError: can only concatenate str (not "int") to str - only a string can be added to another string


# 6:
# Save your hobby to the 'hobby' variable
# Using format method pring following string 'My hobby is <your hobby>.' with completed hobby
# Transform variable date = '2018-11-01' to '01/11' using format
hobby = 'reading'
print('My hobby is {}.'.format(hobby)) # 'My hobby is reading.'
date = '2018-11-01'
day, month = date[-2:], date[5:7]
print('{}/{}'.format(day, month)) # '01/11'


# 7:
# Create list of your hobbies by adding elements to the empty list (the favourite one will be the first)
my_hobbies = ['reading', 'travelling', 'disc golf', 'sewing']

# ● Print the hobby you like most
print(my_hobbies[0]) # 'reading'

# ● Print the hobby you like least
print(my_hobbies[-1]) # 'sewing'

# ● Delete it
my_hobbies.clear()


# 8:
# List of the Czech cities sorted by population size:
cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']

# ● Sort cities in alphabetical order
cities.sort()
print(cities) # ['Brno', 'Ceske Budejovice', 'Hradec Kralove', 'Liberec', 'Olomouc', 'Ostrava', 'Pardubice', 'Plzen', 'Prague', 'Usti nad Labem']

# ● Using "".join() join cities into one string separated by asterix (*)
print("*".join(cities)) # 'Brno*Ceske Budejovice*Hradec Kralove*Liberec*Olomouc*Ostrava*Pardubice*Plzen*Prague*Usti nad Labem'


# 9:
# Find what letters are not present in the Zen of Python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
zen = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea."
letters_not = [letter for letter in alphabet if letter not in zen] # If a letter is not in the Zen of Python, add it to the list
print(letters_not) # ['j', 'q', 'z']

# Another solution (without using list comprehensions):
set_zen = set(zen)
set_alphabet = set(alphabet)
letters_not = set_alphabet.difference(set_zen)
print(letters_not) # {'j', 'q', 'z'}


# 10:
# Fix dictionary and delete erroneous key
d = {'payton':'An interpreted, object-oriented programming language'}
d['Python'] = d['payton']
del d['payton']
print(d) # {'Python': 'An interpreted, object-oriented programming language'}

# 11:
# Use one of the data types and create dictionary, where key will be name and surname (do not put it at one string) and value will be telephone number
d = {('Jussi', 'Korhonen'):'00420123456789'} # Tuple used as the key


# 12:
# You have a dictionary
info = {('Name', 'Surname'):('John', 'Doe')}

# ● Extract dictionary value in following format: 'John_Doe'
person = info[('Name', 'Surname')]
print(person[0] + '_' + person[1]) # 'John_Doe'
