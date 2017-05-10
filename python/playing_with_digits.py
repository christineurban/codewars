# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
  full_num = 0
  counter = 0
    
  for num in str(n):
    full_num += int(num) ** (p + counter)
    counter += 1

  if full_num % n == 0:
    return full_num / n
  else:
    return -1