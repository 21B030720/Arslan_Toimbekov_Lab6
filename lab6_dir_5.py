import os
#   /Users/rabiga/PycharmProjects/lab6
l = ['Arslan', 'Barslan', "Karslan", 'Tarslan']
a = " ".join(l)
with open('a1.txt', 'w') as f:
    f.write(a)
with open('a1.txt', 'r') as f:
    print(f.read())