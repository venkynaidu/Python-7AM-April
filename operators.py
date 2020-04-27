Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10 and 20
20
>>> 20 and 10
10
>>> 100 and 1
1
>>> 10 and 0
0
>>> 0 and 10
0
>>> 10 or 20
10
>>> 20 or 10
20
>>> "Hello" or 0
'Hello'
>>> 10+5j or 0
(10+5j)
>>> -20 or 0
-20
>>> not 10
False
>>> not 0
True
>>> not "Hello"
False
>>> 10 & 5
0
>>> 55 & 60
52
>>> 10 | 5
15
>>> 55 |60
63
>>> 55 ^ 60
11
>>> ~10
-11
>>> 10<<1
20
>>> 10<<2
40
>>> 10<<5
320
>>> 10>>1
5
>>> 7>>1
3
>>> 17>>1
8
>>> 30>>1
15
>>> a=10
>>> 10=a
SyntaxError: can't assign to literal
>>> b=a
>>> b
10
>>> a+=10
>>> a
20
>>> a=23
>>> a*=2
>>> a
46
>>> a=20
>>> b=30
>>> x= a if a<b else b
>>> x
20
>>> x= a if a>b else b
>>> x
30
>>> a=10
>>> b=10
>>> a is b
True
>>> id(a)
140709636174384
>>> id(b)
140709636174384
>>> a==b
True
>>> a is not b
False
>>> s="Hello Venky"
>>> print("Venky" in s)
True
>>> print("venky" in s)
False
>>> print('H' in s)
True
>>> print("Suresh" not in s)
True
>>> 