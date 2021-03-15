def exponent(x):
    i=1
    factorial=1
    z=1
    e=1
    while i<100:
        z=z*x
        factorial = i*factorial
        e=e+z/factorial
        i+=1
    return e

#print(exponent(3.0))

def Ln(x):
    y=0.5*x
    i=1
    numOf_rounds=1
    if x==1:
        y=0
    elif x<0:
        x=-1*x
    while True:
        y=y+2*((x-exponent(y))/(x+exponent(y)))
        i+=1
        numOf_rounds+=1
        if numOf_rounds == 100:
                break
    return y

#print(Ln(100))
    
def XtimesY(x,y):
    if x<0 and y%2!=0:
        z=y*Ln(x)
        x=-exponent(z)
    else:    
        z=y*Ln(x)
        x=exponent(z)
    return x

#print(XtimesY(-5,5))
    
def sqrt(x,y):
    if x==0:
        z=0
    else:
        power=1/x
        z=XtimesY(y,power)
    return z

#print(sqrt(-0.2,14))
    
def calculate(x):
    print(exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x))


x = float(input(''))
calculate(x)
    
    
    
    
  

