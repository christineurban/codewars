# https://www.codewars.com/kata/56a4872cbb65f3a610000026

def max_rot(n):
  n_str = str(n)
  n_lst = []
  biggest = n
   
  for num in n_str:
    n_lst.append(num)
    
  for i in range(len(n_lst)):
    n1 = n_lst.pop(i)
    n_lst.append(n1)
    n_int = int("".join(n_lst))
    
    if n_int > biggest:
      biggest = n_int
      
  return biggest