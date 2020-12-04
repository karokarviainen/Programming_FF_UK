# 4: Write script
# ● Input values: two strings (word and letter) as arguments from command line
# ● Script will print word without specified letter
# ● Example:
# $python extract_letter.py python o
# pythn
# $python extract_letter.py python l
# python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("word", type=str, help="word")
parser.add_argument("letter", type=str, help="letter")

args = parser.parse_args()

result = "" # Create empty string
for character in args.word:
    if character != args.letter:
        result += character # Assign characters to the string

print(result)
