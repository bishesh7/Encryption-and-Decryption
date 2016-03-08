d={'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'june': 6}
q={'jan':1, 'feb':2, 'mar':3, 'apr':6, 'may':6, 'june': 6}

def invert(d):
    b=[]
    c=[]
    for key in d:
        b+=[key]
        c+=[d[key]]
    n={}
    for value in b:
        n[c[b.index(value)]]=value
    if len(n)<len(d):
        return None
    else:
        return n

a=invert(d)
b=invert(q)
print(a)
print(b)
