# https://www.codewars.com/kata/5842df8ccbd22792a4000245

def expanded_form(num):

    num_str = str(num)
    expanded_form = ""
    counter = 1

    for num in num_str:
        num = int(num) * (10 ** (len(num_str) - counter))
        counter += 1
        if num != 0:
          expanded_form += str(num) + " + "
        
    return expanded_form.strip(" + ")