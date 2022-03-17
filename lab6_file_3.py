import os
import re
#polidromes.txt
File = input()
def logic(File):
    l = []
    with open(File, 'r') as f:
        p = f.read()
        l = re.split(r'\n', p)
        print(l)
        print(len(l))
    n = 0
    for i in l:
        if i == i[::-1]:
            print("Polindrome")
            n += 1
        else:
            print("Not Polindrome")
            n += 1
    print(n)

logic(File)