# ● 3: Write script
# ● Input values: two strings as arguments from command line
# ● Script will print number of occurrences of substring in string
# ● Example:
# $python count_occurrence.py ab abcdabcc
# String ab occurred 2 times in string abcdabcc.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("subtext", type=str, help="substring, count number of occurrences of substring in string")
parser.add_argument("text", type=str, help="string, count number of occurrences of substring in string")

args = parser.parse_args()

count = args.text.count(args.subtext) # Count number of occurences
print("String {} occured {} times in string {}.".format(args.subtext, count, args.text))