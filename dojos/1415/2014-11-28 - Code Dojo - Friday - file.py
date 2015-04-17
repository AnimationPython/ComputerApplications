import math



def equation (a,b,c):
    print (-b+math.sqrt(b**2-4*a*c))/(2*a)
    print (-b-math.sqrt(b**2-4*a*c))/(2*a)
equation(2,4,-3)
equation(5,4,-3)
equation(1,8,6)

def celciustofarenheit (c):
    f=(9/5.0)*c+32
    return f
x=celciustofarenheit(100)
print x
print celciustofarenheit(0)
print celciustofarenheit(37)

def farenheittocelcius (far):
    c=(far-32)*(5/9.0)
    return c
print farenheittocelcius(212)
print farenheittocelcius(98.6)
print c
