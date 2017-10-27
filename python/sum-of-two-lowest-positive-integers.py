# https://www.codewars.com/kata/sum-of-two-lowest-positive-integers

def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.remove(min1)
    return min1 + min(numbers)