Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 2
type(a)
<class 'int'>

s = str(a)
s
'2'

type(s)
<class 'str'>

b = complex(2.0, -3.0)
b
(2-3j)

type(b)
<class 'complex'>

b.real
2.0

b.imag
-3.0

desimal = 255
biner = 0b11111111
oktal = 0o377
heksadesimal = 0xff

desimal == biner == oktal == desimal
True


d = 255
bin(d)
'0b11111111'
>>> 
>>> oct(d)
'0o377'
>>> hex(d)
'0xff'
>>> 
>>> 
>>> b = 123.45
>>> type(b)
<class 'float'>
>>> 
>>> b = float('234.567')
>>> b
234.567
>>> type(b)
<class 'float'>
>>> 
>>> 
>>> a = 2e-3
>>> a
0.002
>>> 
>>> b = 2E-3
>>> b
0.002
>>> 
>>> 
>>> import decimal
>>> 
>>> a = 0.012345678909987654321
>>> type(a)
<class 'float'>
>>> 
>>> 
>>> b = decimal.Decimal('0.012345678909987654321')
>>> type(b)
<class 'decimal.Decimal'>
>>> print(b)
0.012345678909987654321
>>> 
>>> 
>>> 0.1 * 3 == 3
False
>>> 
>>> decimal.Decimal('0.1') * 3 == decimal.Decimal('0.3')
True
