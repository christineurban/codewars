# https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order,max_e):
    motive_dict = {}
    answer = []
    
    for motive in order:
      if motive in motive_dict and motive_dict[motive] >= max_e:
        continue
      else:
        motive_dict[motive] = motive_dict.get(motive, 0) + 1
        answer.append(motive)
          
    return answer