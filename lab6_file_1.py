import os
import re
#numbers.txt
def logic(File):
    with open('numbers.txt', 'r') as f:
        sum = 1
        p = f.read()
        m = re.findall(r'[0-9]+', p)
        for i in m:
            i = int(i)
            sum *= i
        print(m)
        print(sum)
logic('numbers.txt')