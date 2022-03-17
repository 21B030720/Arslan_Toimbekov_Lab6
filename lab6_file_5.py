import re
import os
#truth.txt
def logic(File):
    l = []
    with open('truth.txt', 'r') as f:
        p = f.read()
        m = re.findall(r'True|False|true|false', p)
        print(m)
        for i in m:
            if i == "True" or i == "true":
                l.append(True)
            if i == "False" or i == "false":
                l.append(False)
    l = tuple(l)
    print(l)
    l = all(l)
    if l:
        print("True")
    else:
        print("False")


logic('truth.txt')