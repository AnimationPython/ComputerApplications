a=56
b=2.7
c="Good morning. The temperature is "
print b
b*10
print c + str(b*10)

happy=9<10 and 5>3
sad=a==56 or b!=2.7
print sad

x=raw_input("enter a number")
x=float(x)
if x>0:
    print str(x**(0.5))
else:
    print "sorry number must be positive"    

age=float(raw_input("enter your age please"))          
if age>=13 and age<=19:
    print "you're a teenager"
elif age<13:
    print "you're a child"
else:
    print "you're old"
    
