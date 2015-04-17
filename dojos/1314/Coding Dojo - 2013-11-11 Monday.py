Python 2.7.3 |EPD 7.3-1 (32-bit)| (default, Apr 12 2012, 14:30:37) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> hello people :) <3
SyntaxError: invalid syntax
>>> A = 2
>>> A
2
>>> B

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    B
NameError: name 'B' is not defined
>>> B = 4
>>> C = -3
>>> A + B
6
>>> A + C
-1
>>> A + B + C
3
>>> B - C
7
>>> C - B
-7
>>> B - A
2
>>> -A - B
-6
>>> B + A
6
>>> B - -A
6
>>> B*A
8
>>> 10*B
40
>>> B*C
-12
>>> B/A
2
>>> A/B
0
>>> float(A)
2.0
>>> float(A/B)
0.0
>>> float(A)/float(B)
0.5
>>> float(A)/B
0.5
>>> A/float(B)
0.5
>>> A=2.0
>>> A
2.0
>>> A/B
0.5
>>> A**B#
16.0
>>> A**B
16.0
>>> A**2
4.0
>>> C**2
9
>>> B**(1/2)
1
>>> B**float1/2

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    B**float1/2
NameError: name 'float1' is not defined
>>> B**float(1/2)
1.0
>>> B**float(1)/2
2.0
>>> B**0.5
2.0
>>> sqrt(B)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sqrt(B)
NameError: name 'sqrt' is not defined
>>> math.sqrt(B)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    math.sqrt(B)
NameError: name 'math' is not defined
>>> import math
>>> math.sqrt(B)
2.0
>>> price = 361.70
>>> print price/100
3.617
>>> 3.617*17
61.489
>>> 3.617*17.5
63.2975
>>> print price + 63.2975
424.9975
>>> print price + ((price/100)*17.5)
424.9975
>>> v = 9
>>> i = 4
>>> print v/i
2
>>> print v/float(i)
2.25
>>> print float(v)/i
2.25
>>> v = 9.0
>>> print v/i
2.25
>>> A = 2
>>> B = 4
>>> C = -3
>>> print ( -B + math.sqrt(B**2 - ( 4 * A * C )))/ 2*A
2.32455532034
>>> A = 2.0
>>> B = 4.0
>>> C = -3.0
>>> print  ( -B + math.sqrt(B**2 - ( 4 * A * C )))/ 2*A
2.32455532034
>>>  ( -B + math.sqrt(B**2 - ( 4 * A * C )))/ (2*A)
 
  File "<pyshell#62>", line 1
    ( -B + math.sqrt(B**2 - ( 4 * A * C )))/ (2*A)
   ^
IndentationError: unexpected indent
>>> print( -B + math.sqrt(B**2 - ( 4 * A * C )))/ 2*A
2.32455532034
>>> print  ( -B + math.sqrt(B**2 - ( 4 * A * C )))/ (2*A)
0.581138830084
>>> print  ( -B - math.sqrt(B**2 - ( 4 * A * C )))/ (2*A)
-2.58113883008
>>> type ( C )
<type 'float'>
>>> city = string Southampton
SyntaxError: invalid syntax
>>> city = String.southampton

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    city = String.southampton
NameError: name 'String' is not defined
>>> city = "southampton"
>>> city
'southampton'
>>> city [ 5 ]
'a'
>>> city [4]
'h'
>>> city [0]
's'
>>> len city
SyntaxError: invalid syntax
>>> len (city)
11
>>> city [ 12 ]

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    city [ 12 ]
IndexError: string index out of range
>>> city [10]
'n'
>>> city [ len (city) ]

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    city [ len (city) ]
IndexError: string index out of range
>>> city [ len (city) -1 ]
'n'
>>> 
