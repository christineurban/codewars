# https://www.codewars.com/kata/isograms

def is_isogram(string):
    if string:
        return len(set(string.lower())) == len(string)
    return True