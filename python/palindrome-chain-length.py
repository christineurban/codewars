# https://www.codewars.com/kata/palindrome-chain-length

def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    
    special_steps = 0
    
    while str(n) != str(n)[::-1]:
      n += int(str(n)[::-1])
      special_steps += 1
      
    return special_steps 