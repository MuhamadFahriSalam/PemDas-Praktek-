Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(n):
...     import time
...     if n == 0:
...         print('Go!')
...         return
...     print(n, end= ' ')
...     time.sleep(5)
...     f(n-1)
... 
...     
>>> f(3)
3 2 1 Go!
>>> f(10)
10 9 8 7 6 5 4 3 2 1 Go!
