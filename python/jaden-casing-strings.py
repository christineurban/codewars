# https://www.codewars.com/kata/jaden-casing-strings

def toJadenCase(string):
    s_list = string.split()
    for i in range(len(s_list)):
        s_list[i] = s_list[i][0].upper() + s_list[i][1:]
    return " ".join(s_list)