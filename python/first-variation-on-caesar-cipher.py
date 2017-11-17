# http://www.codewars.com/kata/first-variation-on-caesar-cipher

from math import ceil
def moving_shift(s, shift):
    cipher = ''
    curr_shift = shift
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if char.isalpha():
            idx = alpha.index(char.lower())
            new_char = alpha[(idx + curr_shift) % 26]
            if char.isupper():
                cipher += new_char.upper()
            else:
                cipher += new_char
        else:
             cipher += char
        curr_shift += 1
    
    part = ceil(len(cipher) / 5.0)
    total = len(cipher)
    to_run = []
    start_idx = len(cipher)-total
    end_idx = int(part)
    
    while total > 0:
        to_run.append(cipher[int(start_idx):int(end_idx)])
        total -= part
        start_idx = len(cipher)-total
        end_idx += part
        
    if len(to_run) < 5:
        to_run.append('')
    
    return to_run

def demoving_shift(s, shift):
    decoded = ''
    curr_shift = shift
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for char in ''.join(s):
        if char.isalpha():
            idx = alpha.index(char.lower())
            new_char = alpha[(idx - curr_shift) % 26]
            if char.isupper():
                decoded += new_char.upper()
            else:
                decoded += new_char
        else:
             decoded += char
        curr_shift += 1
    
    return decoded