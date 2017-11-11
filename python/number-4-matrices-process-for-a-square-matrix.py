# http://www.codewars.com/kata/number-4-matrices-process-for-a-square-matrix

def avg_diags(m):
    m_length = len(m)
    avg1 = []
    avg2 = []
    for i in range(len(m)):
        if i % 2 == 1:
            if m[i][i] >= 0:
                avg1.append(m[i][i])
        else:
            if m[len(m)-1-i][i] < 0:
                avg2.append(m[len(m)-1-i][i])
    if avg1:
        avg1 = round(sum(avg1)/len(avg1))
    else:
        avg1 =-1
    if avg2:
        avg2 = round(abs(sum(avg2)/len(avg2)))
    else:
        avg2 = -1
    return [avg1, avg2]