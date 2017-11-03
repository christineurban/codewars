# https://www.codewars.com/kata/is-this-a-triangle

def is_triangle(a, b, c):
    longest = max(a, b, c)
    if a + b + c - longest > longest:
        return True
    return False