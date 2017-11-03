# https://www.codewars.com/kata/highest-and-lowest

def high_and_low(numbers):
    num_list = numbers.split()
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return "{} {}".format(max(num_list), min(num_list))