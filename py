def reverese(S):
    l=[i for i in S]
    k=''
    while len(l)>0:
        k=k+l.pop()
    return k
