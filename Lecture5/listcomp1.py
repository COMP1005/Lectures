"""
listcomp1.py - list comprehension examples

COMP1005/5005 updated 25/3/24

Usage guide:
    - just run it :)

"""

# unconditional list comprehension

numbers = [1, 2, 3, 4, 5]

doubled_numbers = []
for n in numbers:
    doubled_numbers.append(n * 2)

print(doubled_numbers)

doubled_numbers = [n * 2 for n in numbers]

print(doubled_numbers)

# conditional list comprehension

doubled_odds = [] 
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)

print(doubled_odds)

doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

print(doubled_odds)
