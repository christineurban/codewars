# https://www.codewars.com/kata/money-money-money

def calculate_years(principal, interest, tax, desired):
    current = principal
    years = 0
    while current < desired:
        current += current * interest - (current * interest * tax)
        years += 1
    return years