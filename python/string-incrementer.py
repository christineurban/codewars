# http://www.codewars.com/kata/string-incrementer

def increment_string(strng):
    num = ''
    word = ''
    rev = strng[::-1] 
    for i in range(len(rev)):
        try:
            num = str(int(rev[i])) + num
        except:
            word = rev[i:][::-1]
            break
    if num:
        new_num = str(int(num)+1)
        if len(new_num) == len(num):
            return word + new_num
        else:
            return word + ('0' * (len(num)-len(new_num))) + new_num
    else:
        return word + '1'