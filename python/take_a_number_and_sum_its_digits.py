# https://www.codewars.com/kata/5626b561280a42ecc50000d1

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    dig_pow_list = []
    dig_pow = 0
    
    for num in range(a, b + 1):
        counter = 0
        dig_pow = 0
        for digit in str(num):
            counter += 1
            dig_pow += int(digit) ** counter

        if num == dig_pow:
            dig_pow_list.append(num)

    return dig_pow_list