# https://www.codewars.com/kata/57b6f850a6fdc76523001162

def counter_effect(hit_count):
  hit_count = list(hit_count)
  answer = []
  
  for num in hit_count:
    num_list = []
    
    for i in range(0, int(num) + 1):
      num_list.append(i)
    
    answer.append(num_list)

  return answer