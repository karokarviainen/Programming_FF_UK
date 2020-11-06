# 1:
# You have list of top 20 names in Czech Republic
names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 'Lenka', 'Katerina']
# ● Write code that Ask user for their name (reminder use: input(‘Your name’))
# ○ Check if name is in the list (reminder use: in)
# ■ If name is in the list then it prints reply
# ■ If name is not in the list then it prints another reply
user_name = input("Enter your name: ").capitalize()
if user_name in names_list:
    print("Cool name!")
else:
    print("Not so cool name.")

print()


# 2:
# You have international spelling alphabet
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}
# ● Write code that will: a) Ask user's name, b) Spell user's name
user_name2 = input("Enter your name: ").lower()
for letter in user_name2:
    print(letter, d[letter])

print()


# 3:
#  Transpose following list using both nested loops and list comprehensions
# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# To this list:
# b = [[1,4,7],
#      [2,5,8],
#      [3,6,9]]


# 4:
# Create shopping list
# ● Using for and break write code that: ○ Will ask for new item, ○ Go through the list
# ○ If item is found then: ■ Print item, ■ Stop searching
# ○ If item is not found: ■ Append item to the list

shopping_list = ["potatoes", "apples", "chicken", "soy sauce", "milk", "bananas"]
new_item = input("New item: ")
if new_item in shopping_list:
    print(new_item)
else:
    shopping_list.append(new_item)
    print(shopping_list)

print()


# 5:
# Create list containing 5 numbers
nums = list(range(1, 6))
print(nums) # [1, 2, 3, 4, 5]

# ○ Using list comprehensions create list where:
# ■ Each element is multiplied by itself (E.g. 5 → 25)
nums_mult = [num * num for num in nums]
print(nums_mult) # [1, 4, 9, 16, 25]

# ■ 'is my favorite number!' is added to each element of the list' (E.g. '5 is my favorite number!')
fav_nums = ["{} is my favorite number!".format(num) for num in nums]
print(fav_nums) # ['1 is my favorite number!', '2 is my favorite number!', '3 is my favorite number!', '4 is my favorite number!', '5 is my favorite number!']

print()


# 6:
#  Using list comprehensions write code that
# ○ Takes string as an input, e.g. seq = 'ACTGCTCAAG'
# ○ Creates list with positions where 'A' is occurring, e.g. pos = [0, 7, 8]
# ○ Prints created list
# ○ Hint: use enumerate()
# ● BONUS task: come up with the second solution
user_input = input("Enter a string: ") # 'ACTGCTCAAG'
positions = [i for i, letter in enumerate(user_input) if letter == "A"]
print(positions) # [0, 7, 8]

print()


# 7:
# You have dictionary of points in competition
scores = {'John' : 10, 'Emily' : 35, 'Matthew' : 50}
# ○ Using dictionary comprehensions, create dictionary, where everyone gets triple amount of points
new_scores = {name:scores[name] * 3 for name in scores}
print(new_scores) # 'John': 30, 'Emily': 105, 'Matthew': 150}