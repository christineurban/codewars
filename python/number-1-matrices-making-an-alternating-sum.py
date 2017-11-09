# http://www.codewars.com/kata/number-1-matrices-making-an-alternating-sum

def score_matrix(matrix):
    rows = []
    for i in range(len(matrix)):
        # if even row start with adding
        if i % 2 == 0:
            add = True
        # if odd row start with subtracting
        else:
            add = False
        
        row_sum = 0
        
        for num in matrix[i]:
            if add:
                row_sum += num
                add = False
            else:
                row_sum -= num
                add = True
        rows.append(row_sum)
    return sum(rows)