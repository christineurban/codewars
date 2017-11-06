# https://www.codewars.com/kata/find-the-next-perfect-square

def find_next_square(sq):
    if (sq**0.5).is_integer():
        return (int(sq**0.5) + 1) ** 2
    return -1