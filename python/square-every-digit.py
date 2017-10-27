# https://www.codewars.com/kata/square-every-digit

def square_digits(num):
    return int(''.join([str(int(x)**2) for x in str(num)]))