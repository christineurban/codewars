# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    s = source_array
    odds = []
    for i in range(len(s)):
        if s[i] % 2 != 0:
            odds.append(s[i])
            s[i] = "x"
    
    odds.sort()
    for i in range(len(s)):
        if s[i] == "x":
            s[i] = odds.pop(0)
            
    return s