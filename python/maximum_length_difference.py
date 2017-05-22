# https://www.codewars.com/kata/5663f5305102699bad000056

def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    else:
        x_sml = len(a1[0])
        x_lrg = len(a1[0])
        y_sml = len(a2[0])
        y_lrg = len(a2[0])
        
        for s1 in a1:
            if len(s1) <= x_sml:
                x_sml = len(s1)
            elif len(s1) > x_lrg:
                x_lrg = len(s1)
        
        for s2 in a2:
            if len(s2) <= y_sml:
                y_sml = len(s2)
            elif len(s2) > y_lrg:
                y_lrg = len(s2)
        
               
        if abs(x_sml-y_lrg) >= abs(x_lrg-y_sml):
            return abs(x_sml-y_lrg)
        else:
          return abs(x_lrg-y_sml)