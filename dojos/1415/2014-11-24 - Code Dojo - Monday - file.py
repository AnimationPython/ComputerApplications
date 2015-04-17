c=100
f=c*(9/5.0)+32
print f
def c2f(c):
    f=c*(9/5.0)+32
    return f
print c2f(100)
print c2f(0)
print c2f(37)
print c2f(4)
print c2f(-2)

def f2c(f):
    c=(f-32)/(9/5.0)
    return c
print f2c(98.6)
print f2c(28.4)
print f2c(212)

def roots(a, b, c):
    x1=(-b+(b**2-4*a*c)**(0.5))/(2*a)
    x2=(-b-(b**2-4*a*c)**(0.5))/(2*a)
    return [x1, x2]
print roots(2, 4, -3)

