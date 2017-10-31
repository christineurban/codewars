# https://www.codewars.com/kata/mumbling

def accum(s):
    mumble = ""
    for i in range(len(s)):
        mumble += s[i].upper()
        mumble += s[i].lower() * i
        if i+1 != len(s):
            mumble += "-"
    return mumble