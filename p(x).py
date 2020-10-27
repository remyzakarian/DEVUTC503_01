def p(x,a,n):
    i=0
    rep=0
    while(i<=n):
        rep = rep + ((a*i)*(x*i))
        i = i+1
    print(rep)
