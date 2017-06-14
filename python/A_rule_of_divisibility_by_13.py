# https://www.codewars.com/kata/564057bc348c7200bd0000ff

def thirt(n):
    curr_num = n
    last_num = 0
    
    rem = [1, 10, 9, 12, 3, 4]
    
    while curr_num != last_num:
      n = str(curr_num)[::-1]
      last_num = curr_num
      curr_num = 0
      
      for i in range(len(n)):
        try:    
          curr_num += (int(n[i]) * rem[i])
        except:
          curr_num += (int(n[i]) * rem[i%6])
    
        
    return curr_num