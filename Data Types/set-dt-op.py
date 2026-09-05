Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py
{True, 'razin', 3j, 10, 25.5}
>>> 
= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py
{True, 3j, 10, 25.5, 'razin'}
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py", line 16, in <module>
    print(s[1])
TypeError: 'set' object is not subscriptable
>>> 
= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py
{'razin', True, 3j, 10, 25.5}
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py", line 19, in <module>
    print(s[1:4])
TypeError: 'set' object is not subscriptable
>>> 
= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py
{'razin', True, 3j, 10, 25.5}
{'razin', True, 200, 3j, 10, 25.5}
>>> 
= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py
{True, 'razin', 3j, 10, 25.5}
{True, 'razin', 200, 3j, 10, 25.5}
{True, 200, 3j, 10, 25.5}
>>> 
= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py
{True, 'razin', 3j, 10, 25.5}
{True, 'razin', 200, 3j, 10, 25.5}
{True, 200, 3j, 10, 25.5}
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/Data Types/set-dt.py", line 30, in <module>
    s.min()
AttributeError: 'set' object has no attribute 'min'
