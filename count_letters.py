# 2: Write a small Python script count_letters.py using argparse that:
# - Has a positional argument of the string in which letters are supposed to be
# counted.
# - Has two optional arguments:
# - v: to count only vowels
# - c: count only consonants
# The script prints out a list of letters in alphabetical order with the number of
# occurrences:
# a 2
# b 5

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str, help="count occurence of each letter")
parser.add_argument("-v", "--vowel", action="store_true", help="count only vowels")
parser.add_argument("-c", "--consonant", action="store_true", help="count only consonants")

args = parser.parse_args()

char_count = {}
for i in args.text: # Make dictionary with letters as keys and number of occurences as values
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]

for key in sorted(char_count): # Select correct letters (vowels/consonants/all from the dictionary and print them)
    if args.vowel:
        if key in vowels:
            print(key, char_count[key])
    elif args.consonant:
        if key not in vowels:
            print(key, char_count[key])
    else:
        print(key, char_count[key])