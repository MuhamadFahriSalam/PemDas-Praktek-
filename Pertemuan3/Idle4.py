Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 2
>>> b = a
>>> c = 3
>>> id(a)
140708891218760
>>> id(b)
140708891218760
>>> id(c)
140708891218792
>>> a is b
True
>>> a is c
False
>>> a is not b
False
>>> a is not c
True
