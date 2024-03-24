"""
listcomp3.py - list comprehension examples with strings, functions and indexing

COMP1005/5005 updated 25/3/24

Usage guide:
    - just run it :)

"""
fullname = ["Arthur","King","Of","The","Britons"]
initials = [word[0] for word in fullname]
print(initials)

# ['A', 'K', 'O', 'T', 'B']

lowered = [x.lower() for x in ["F","O","P"] ]
print(lowered)

# ['f', 'o', 'p']

