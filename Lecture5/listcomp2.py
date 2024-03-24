"""
listcomp2.py - list comprehension examples with functions

COMP1005/5005 updated 25/3/24

Usage guide:
    - just run it :)

"""

def double(x):
    return x*2

list1 = [3,4,5]
multiplied = [item*3 for item in list1]

# [9,12,15]
print(multiplied)

doubled = [double(x) for x in range(10)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(doubled)

doubled = [double(x) for x in ["a","b","c"]]
# [“aa”, “bb”, “cc”]
print(doubled)

