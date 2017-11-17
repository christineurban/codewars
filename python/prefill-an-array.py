# http://www.codewars.com/kata/prefill-an-array

def prefill(n,v=0):
    try:
        if n == 0 or int(n) == 0:
            return []
    except:
        if not isinstance(n, int):
            try:
                return [v for x in range(int(n))]
            except:
                raise TypeError('{} is invalid'.format(n))
    if not v:
        return [v]
    return [v for x in range(int(n))]