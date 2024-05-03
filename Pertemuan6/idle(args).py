Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(*args):
...     print('Nilai *args\t: %s' % repr(args))
...     print('Tipe *args\t: %s' % type(args))
... 
>>> f(1)
Nilai *args	: (1,)
Tipe *args	: <class 'tuple'>
>>> f(1, 2)
Nilai *args	: (1, 2)
Tipe *args	: <class 'tuple'>
>>> f(1, 2, 3)
Nilai *args	: (1, 2, 3)
Tipe *args	: <class 'tuple'>
