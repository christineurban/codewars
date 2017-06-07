# https://www.codewars.com/kata/54b80308488cb6cd31000161

def group_check(s):
    print s

    if s == "":
        return True

    open = ['(', '{', '[']
    close = [')', '}', ']']
    ol = []
    
    if s[0] not in open or s[-1] not in close:
        return False
        
    for char in s:
        if char in open:
            ol.append(open.index(char))
        elif char in close:
            if len(ol) == 0:
                return False
            if char == close[ol[-1]]:
                ol.pop()
            else:
               return False
            
    if len(ol) > 0:
        return False
    
    return True