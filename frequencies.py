"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):
    frequencies = {}
    # Your code goes here
    newList = []
    for item in items:
        newList.append(str(item))
    items = newList
    frequencies = {x:items.count(x) for x in items}

    return frequencies
