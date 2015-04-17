Python 2.7.3 |EPD 7.3-1 (32-bit)| (default, Apr 12 2012, 14:30:37) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Paul = James

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Paul = James
NameError: name 'James' is not defined
>>> A = 7
>>> A
7
>>> B = A * 2
>>> B
14
>>> A = 10
>>> B
14
>>> B / 3
4
>>> B / 3.0
4.666666666666667
>>> C = 25
>>> C**0.5
5.0
>>> sqrt(C)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sqrt(C)
NameError: name 'sqrt' is not defined
>>> math.sqrt(C)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    math.sqrt(C)
NameError: name 'math' is not defined
>>> import math
>>> math.sqrt(C)
5.0
>>> sqrt(C)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sqrt(C)
NameError: name 'sqrt' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
72.34
>>> ================================ RESTART ================================
>>> 
72.34

Traceback (most recent call last):
  File "H:/Computer Applications/1Codedojo monday", line 8, in <module>
    x = (-b+((b**2)(-4*a*c))**0.5)/2*a
TypeError: 'int' object is not callable
>>> ================================ RESTART ================================
>>> 
72.34
2.32455532034
>>> ================================ RESTART ================================
>>> 
72.34
2.32455532034
-10.3245553203
>>> ================================ RESTART ================================
>>> 
72.34
0.581138830084
-2.58113883008
>>> ================================ RESTART ================================
>>> 
72.34

Traceback (most recent call last):
  File "H:/Computer Applications/1Codedojo monday", line 8, in <module>
    x = (-b+((b**2)-4*a*c)**0.5)/(2*a)
ValueError: negative number cannot be raised to a fractional power
>>> ================================ RESTART ================================
>>> 
72.34
-0.161483519287
-1.23851648071
>>> name = Paul

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    name = Paul
NameError: name 'Paul' is not defined
>>> name = "Paul"
>>> name
'Paul'
>>> print "Hello, my name is" & name

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print "Hello, my name is" & name
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> print "Hello, my name is" + name
Hello, my name isPaul
>>> print "Hello, my name is " + name
Hello, my name is Paul
>>> print "Hello, my name is " + name + ". Nice to meet you!"
Hello, my name is Paul. Nice to meet you!
>>> name[1]
'a'
>>> name[2]
'u'
>>> name[0]
'P'
>>> name[4]

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name[4]
IndexError: string index out of range
>>> len(name)
4
>>> name[len(name)]

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name[len(name)]
IndexError: string index out of range
>>> name[len(name-1)]

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    name[len(name-1)]
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> name[len(name)-1]
'l'
>>> Yay!
SyntaxError: invalid syntax
>>> name[2:3]
'u'
>>> name[1:3]
'au'
>>> name[:3]
'Pau'
>>> name[1:]
'aul'
>>> name.upper()
'PAUL'
>>> name.lower()
'paul'
>>> name.capitalize()
'Paul'
>>> 
