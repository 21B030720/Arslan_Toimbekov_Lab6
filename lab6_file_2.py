import os
import re
#text.txt
def logic(File):
    with open(File, 'r') as f:
        p = f.read()
        m1 = re.findall(r'[A-Z]', p)
        m2 = re.findall(r'[a-z]', p)
        print("Big letters:", len(m1))
        print("Low letters:", len(m2))
logic('text.txt')