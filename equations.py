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
    return float(e)


def Ln(x):
    y=0.5*x
    i=1
    numOf_rounds=1
    if x==1:
        y=0
    elif x<=0:
        y=0
    else:
        while True:
            y=y+2*((x-exponent(y))/(x+exponent(y)))
            i+=1
            numOf_rounds+=1
            if numOf_rounds == 100:
                break
    return float(y)


 
def XtimesY(x,y):
    if x<0:
        x=0
    else:    
        z=y*Ln(x)
        x=exponent(z)
    return float(x)

    
def sqrt(x,y):
    if x==0:
        z=0
    else:
        power=1/x
        z=XtimesY(y,power)
    return float(z)

    
def calculate(x):
    result=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    result = float('%0.6f' % result)
    return float(result)

    
    
    
  

