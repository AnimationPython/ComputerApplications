Python 2.7.3 |EPD 7.3-1 (32-bit)| (default, Apr 12 2012, 14:30:37) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 6
>>> s
6
>>> s
6
>>> ================================ RESTART ================================
>>> 
7
>>> ================================ RESTART ================================
>>> 
7
>>> ================================ RESTART ================================
>>> 
7
>>> execfile(Test.py)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    execfile(Test.py)
NameError: name 'Test' is not defined
>>> execfile("Test.py")
7
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
3.60555127546
>>> ================================ RESTART ================================
>>> 
Enter a value 16

Traceback (most recent call last):
  File "H:/Test.py", line 3, in <module>
    t = math.sqrt (s)
TypeError: a float is required
>>> ================================ RESTART ================================
>>> 
Enter a value 16

Traceback (most recent call last):
  File "H:/Test.py", line 3, in <module>
    t = math.sqrt (s)
TypeError: a float is required
>>> ================================ RESTART ================================
>>> 
Enter a value 16
4.0
>>> ================================ RESTART ================================
>>> 
Enter a value -13

Traceback (most recent call last):
  File "H:/Test.py", line 4, in <module>
    t = math.sqrt (s)
ValueError: math domain error
>>> ================================ RESTART ================================
>>> 
Enter a value 19
4.35889894354
>>> ================================ RESTART ================================
>>> 
Enter a value -12
>>> ================================ RESTART ================================
>>> 
Enter a value -8
That is not a vaild entry
>>> teachers = [Riki,Yvonne]

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    teachers = [Riki,Yvonne]
NameError: name 'Riki' is not defined
>>> teachers = ["Riki","Yvonne"]
>>> teachers
['Riki', 'Yvonne']
>>> teachers[1]
'Yvonne'
>>> teachers[1[4]]

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    teachers[1[4]]
TypeError: 'int' object has no attribute '__getitem__'
>>> y = teachers[1]
>>> y
'Yvonne'
>>> y[4]
'n'
>>> teachers[1][4]
'n'
>>> 6 * 2
12
>>> 6 * 2 - 3
9
>>> 6 * (2 - 3)
-6
>>> teachers.append ("Michael")
>>> teachers
['Riki', 'Yvonne', 'Michael']
>>> len(teachers)
3
>>> for teacher in teachers:
	print teacher

	
Riki
Yvonne
Michael
>>> for x in teachers
SyntaxError: invalid syntax
>>> for x in teachers:
	print x

	
Riki
Yvonne
Michael
>>> for x in teachers:
	l= len(x)
	print l

	
4
6
7
>>> total = 0
>>> for x in teachers:
	l=len(x)
	total=(total+l)

	
>>> print total
17
>>> 
