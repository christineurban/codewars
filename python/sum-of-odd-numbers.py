# https://www.codewars.com/kata/sum-of-odd-numbers

def row_sum_odd_numbers(n):
    row_start = 1
    for i in range(n):
        row_start += i*2
    print row_start
    row_total = row_start
    for i in range(n-1):
        row_total += row_start + (i+1)*2
    return row_total