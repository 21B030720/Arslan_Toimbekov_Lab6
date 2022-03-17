import os
with open('a1.txt', 'r') as f:
    p = f.read()
    with open('a2.txt', 'w') as k:
        k.write(p)
with open('a2.txt', 'r') as f:
    print(f.read())