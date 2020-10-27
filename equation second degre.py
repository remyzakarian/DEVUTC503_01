
from math import sqrt
def seconddegre(a, b , c):
    delta = pow(b,2)-4*(a*c)
    print("delta est : ",delta)

    if(delta > 0):
        rep1 = (-b-sqrt(delta))
        rep2 = (-b+sqrt(delta))
        rep1 = rep1/(2*a)
        rep2 = rep2/(2*a)
        print("reponse 1 :",rep1)
        print("reponse 2 :",rep2)
    if(delta == 0):
        rep3 = (-b/(2*a))
        print("reponse : ",rep3)
    if(delta < 0):
        print("il n y a pas de solution")
