def pluspetitdiviseur(n):
    i=1
    while(i<=n):
        if(n == 1):
            print("le plus petit diviseur de 1 est 1")
        if(i==1):
            i=i+1
        else:
            if(n%i != 0):
                i = i+1
            else:
                if(n%i == 0):
                    print("le plus petit diviseur autre que 1 est : ",i)
                    return