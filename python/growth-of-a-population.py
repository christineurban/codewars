# https://www.codewars.com/kata/growth-of-a-population

def nb_year(p0, percent, aug, p):
    current_pop = p0
    years = 0
    
    while current_pop < p:
        years += 1
        current_pop += current_pop * (percent/100) + aug
    
    return years