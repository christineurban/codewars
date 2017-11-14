# https://www.codewars.com/kata/disemvowel-trolls

def disemvowel(string):
    vowels = "AaEeIiOoUu"
    no_vowels = ""
    for char in string:
        if char not in vowels:
            no_vowels += char
    return no_vowels