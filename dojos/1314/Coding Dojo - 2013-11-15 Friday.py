Python 2.7.3 |EPD 7.3-1 (32-bit)| (default, Apr 12 2012, 14:30:37) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> "welcome to the coding dojo"
'welcome to the coding dojo'
>>> a = 2
>>> 2 == a
True
>>> 2 = a
SyntaxError: can't assign to literal
>>> a = 2
>>> 2 = a
SyntaxError: can't assign to literal
>>> b = 4
>>> c = -3
>>> a |+ b
6
]
>>> a + b
6
>>> a + c
-1
>>> a + b + c
3
>>> c - b
-7
>>> b -c
7
>>> a - b
-2
>>> -a - b
-6
>>> b - -a
6
>>> b --a
6
>>> a * b
8
>>> b * 10
40
>>> c * b
-12
>>> b /a
2
>>> a / b
0
>>> 0.5
0.5
>>> int(1.9)
1
>>> float(1.9)
1.9
>>> float(a)
2.0
>>> float(a) / b
0.5
>>> a / float(b)
0.5
>>> float(a) / float(b)
0.5
>>> a**b
16
>>> a**2
4
>>> c**3
-27
>>> B**0.5

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    B**0.5
NameError: name 'B' is not defined
>>> b**0.5
2.0
>>> sqrt(b)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sqrt(b)
NameError: name 'sqrt' is not defined
>>> math.sqrt(b)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    math.sqrt(b)
NameError: name 'math' is not defined
>>> import math
>>>  math.sqrt(b)
 
  File "<pyshell#38>", line 1
    math.sqrt(b)
   ^
IndentationError: unexpected indent
>>> math.sqrt(b)
2.0
>>> c**2
9
>>> math.sqrt(c)

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    math.sqrt(c)
ValueError: math domain error
>>> price = 361.70
>>> vat = 0.175*price
>>> vat =
SyntaxError: invalid syntax
>>> vat
63.29749999999999
>>> price + vat
424.9975
>>> total = price + vat
>>> total
424.9975
>>> round(total)
425.0
>>> round(total,2)
425.0
>>> price + (price*0.175)
424.9975
>>> voltage = 9
>>> i = 4
>>> restiance = voltage / i
>>> restiance
2
>>> float(voltage) / i
2.25
>>> voltage = float(9)
>>> restiance = voltage / i
>>> restiance
2.25
>>> print Hi Guys
SyntaxError: invalid syntax
>>> print "Hi Guys"
Hi Guys
>>> a=2
>>> b=4
>>> c=-3
>>> (-b+(sqrt((b**2)-(4*a*c))/(2*a)
     blob = (-b+(sqrt((b**2)-(4*a*c))/(2*a)
		 
SyntaxError: invalid syntax
>>> blob = (-b+(sqrt((b**2)-(4*a*c))/(2*a)
print blob
	    
SyntaxError: invalid syntax
>>> (-b+(sqrt((b**2)-(4*a*c))))/(2*a)

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    (-b+(sqrt((b**2)-(4*a*c))))/(2*a)
NameError: name 'sqrt' is not defined
>>> (-b+(math.sqrt((b**2)-(4*a*c))/(2*a)
     (-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)))

Traceback (most recent call last):
  File "<pyshell#75>", line 2, in <module>
    (-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)))
TypeError: 'int' object is not callable
>>> ((-b+(math.sqrt((b**2)-(4*a*c))))/(2*a))
0.5811388300841898
>>> ((-b-(math.sqrt((b**2)-(4*a*c))))/(2*a))
-2.58113883008419
>>> blob=((-b+(math.sqrt((b**2)-(4*a*c))))/(2*a))
>>> type(blob)
<type 'float'>
>>> city="Southampton"
>>> city(5)

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    city(5)
TypeError: 'str' object is not callable
>>> count.city(5)

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    count.city(5)
NameError: name 'count' is not defined
>>> city[5]
'a'
>>> city[4]
'h'
>>> city[0]
'S'
>>> city[1]
'o'
>>> city[12]

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    city[12]
IndexError: string index out of range
>>> city[11]

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    city[11]
IndexError: string index out of range
>>> city[10]
'n'
>>> len(city)
11
>>> city[len(city)]

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    city[len(city)]
IndexError: string index out of range
>>> x=len(city)
>>> city[x]

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    city[x]
IndexError: string index out of range
>>> city[(x-1)]
'n'
>>> city="Manchester"
>>> len(city)
10
>>> x=len(city)
>>> city[x-1]
'r'
>>> city="Southampton"
>>> city[4:7]
'ham'
>>> city[:5]
'South'
>>> city[-1]
'n'
>>> city[-2]
'o'
>>> city[-1:-7]
''
>>> city[-7:]
'hampton'
>>> city[:2]
'So'
>>> city[-3:]
'ton'
>>> print city[:2]+city[-3:]
Soton
>>> print city[:2]+"'"+city[-3:]
So'ton
>>> 
