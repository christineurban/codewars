# hhttps://www.codewars.com/kata/54da539698b8a2ad76000228

def isValidWalk(walk):
    ns = 0
    ew = 0
    for direction in walk:
        if direction == 'n':
            ns += 1
        elif direction == 's':
            ns -= 1
        elif direction == 'e':
            ew += 1
        else:
            ew -= 1
            
    if ns == 0 and ew == 0:
        return True
    else:
        return False