import os
#   /Users/rabiga/PycharmProjects/lab6

def CheckThePath(path, n):
    print("The Head: ", os.path.dirname(path))
    print("The Tail: ", os.path.basename(path))
    if os.path.exists(path):
        print("This searched exists")
    else:
        print("This searched doesn't exist")



path = input()
CheckThePath(path, 0)