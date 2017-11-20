# http://www.codewars.com/kata/identifying-top-users-and-their-corresponding-purchases-on-a-website

def id_best_users(*args):
    purchases = {}
    mo = {}
    for arg in args:
        temp = set()
        for id in arg:
            purchases[id] = purchases.get(id, 0) + 1
            temp.add(id)
        for id in temp:
            mo[id] = mo.get(id, 0) + 1
    
    all_mo = [k for k, v in mo.items() if v >= len(args)]
    temp = []
    for id in purchases:
        if id not in all_mo:
            temp.append(id)
    for id in temp:
        del purchases[id]   
    
    best = {}
    for k,v in purchases.items():
        best[v] = best.get(v, [])
        best[v].append(k)
    return [[k, sorted(v)] for k, v in sorted(best.items(), reverse=True)]