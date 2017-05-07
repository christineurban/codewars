# https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(ints, s):
    prev_num = None
    for i in range(len(ints)):
      if ints[i] == prev_num:
          continue
      prev_num = ints[i]
      counter = i
      while counter != 0:
        counter -= 1
        if ints[i] + ints[counter] == s:
          return [ints[counter], ints[i]]