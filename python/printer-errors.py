# https://www.codewars.com/kata/printer-errors

def printer_error(s):
    colors = "abcdefghijklm"
    non_colors = 0
    for color in s:
        if color not in colors:
            non_colors += 1
    return "{}/{}".format(non_colors, len(s))