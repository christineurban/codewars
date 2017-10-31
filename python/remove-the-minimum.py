# https://www.codewars.com/kata/remove-the-minimum

def remove_smallest(numbers):
    ratings = numbers
    if ratings:
        ratings.remove(min(numbers))
    return ratings