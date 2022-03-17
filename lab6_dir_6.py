import os
a = ord("A")
for i in range(26):
    print(chr(a+i), end = " ")
for i in range(26):
    s = f'{chr(a+i)}.txt'
    open(s, 'x')
