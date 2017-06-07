# https://www.codewars.com/kata/5512e5662b34d88e44000060

def find_missing_number(sequence):
  if sequence == "":
    return 0

  try:
    seq = map(int, sequence.split())
  except:
    return 1
  
  seq.sort()

  for i in range(len(seq)):
    if (i + 1) == seq[i]:
      continue
    else:
      return (i + 1)
      
  return 0