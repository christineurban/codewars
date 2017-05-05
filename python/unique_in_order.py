# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
  try:
    chars = list(iterable)
    unique = [chars[0]]
    counter = 0

    for char in chars[1:]:
      if char == chars[counter]:
        counter += 1
        continue
      else:
        unique.append(char)
        counter += 1
  except:
    return []

  return unique