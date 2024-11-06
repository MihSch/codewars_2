"""An isogram is a word that has no repeating letters,
consecutive or non-consecutive. Implement a function that determines
whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case."""

def is_isogram(string):
    # your code here
    set_string = set(string.lower())
    if len(string.lower()) == len(set_string):
        a = True
    else:
        a = False
    return a