import numpy as np
F=lambda x:x**2+2

def Trapezoidal(a,b,n):
    h=(b-a)/n;res=F(a)+F(b)
    for i in range(1,n):res+=2*F(a+i*h)
    return res*h/2

def Simpson13(a,b,n):
    if n%2:return None
    h=(b-a)/n;res=F(a)+F(b)
    for i in range(1,n):res+=4*F(a+i*h) if i%2 else 2*F(a+i*h)
    return res*h/3

def Simpson38(a,b,n):
    if n%3:return None
    h=(b-a)/n;res=F(a)+F(b)
    for i in range(1,n):res+=2*F(a+i*h) if i%3==0 else 3*F(a+i*h)
    return res*3*h/8

def Boole(a,b,n):
    if n%4:return None
    h=(b-a)/n;res=F(a)+F(b)
    for i in range(1,n):
        res+={0:14,2:12}.get(i%4,32)*F(a+i*h)
    return res*2*h/45

def Weddle(a,b,n):
    if n%6:return None
    h=(b-a)/n;res=F(a)+F(b)
    for i in range(1,n):
        res+=(2 if i%6==0 else 6 if i%3==0 else 1 if i%2==0 else 5)*F(a+i*h)
    return res*3*h/10

def GaussLegendre3P(a,b):
    w=[5/9,8/9,5/9];z=[-np.sqrt(3/5),0,np.sqrt(3/5)]
    P=(b-a)/2;Q=(a+b)/2;x=P*np.array(z)+Q
    return P*np.dot(F(x),w)

def safe_print(name,val):print(f"{name}: {val:.6f}" if val is not None else f"{name}: Invalid n")

if __name__=="__main__":
    a,b,n=2,3,6
    print("Integration of f(x)=x²+2 from 2 to 3\n"+"="*40)
    safe_print("Trapezoidal",Trapezoidal(a,b,n))
    safe_print("Simpson 1/3",Simpson13(a,b,n))
    safe_print("Simpson 3/8",Simpson38(a,b,n))
    safe_print("Boole",Boole(a,b,n))
    safe_print("Weddle",Weddle(a,b,n))
    safe_print("Gauss-Legendre 3P",GaussLegendre3P(a,b))
    analytical=(3**3/3+2*3)-(2**3/3+2*2)
    print(f"Analytical: {analytical:.6f}\n"+"="*40)
