import os
import re
#   /Users/rabiga/PycharmProjects/lab6

def Search(path, n):
    while(os.path.exists(path) != True):
        print("Search again")
        path = input()
        Search(path, n)
    else:
        with open(path, 'r') as f:
            p = f.read()
            print(p.count("\n") + 1)
            return 0

path = input()
Search(path, 0)