# https://www.codewars.com/kata/shortest-word

def find_short(s):
    return min([len(x) for x in s.split()])