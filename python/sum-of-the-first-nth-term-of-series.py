# https://www.codewars.com/kata/sum-of-the-first-nth-term-of-series

def series_sum(n):
    answer = 0.00
    fraction = 1
    
    for i in range(n):
        answer += 1/float(fraction)
        fraction += 3
        
    return "{0:.2f}".format(answer)