Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(**kwargs):
...     print('Nilai **kwargs\t: %s' % repr(kwargs))
...     print('Tipe **kwargs\t: %s' % type(kwargs))
... 
...     
>>> f(satu=1, dua=2)
Nilai **kwargs	: {'satu': 1, 'dua': 2}
Tipe **kwargs	: <class 'dict'>
>>> f(satu=1, dua=2, tiga=3)
Nilai **kwargs	: {'satu': 1, 'dua': 2, 'tiga': 3}
Tipe **kwargs	: <class 'dict'>
