# https://www.codewars.com/kata/descending-order

def Descending_Order(num):
    return int("".join(sorted(list(str(num)), reverse=True)))