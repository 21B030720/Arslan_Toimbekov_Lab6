import os
#   /Users/rabiga/PycharmProjects/lab6
def step(n):
    print("<<|"*n, end = "")

def ShowAll(path, n):
    for target in os.listdir(path):
        target_path = os.path.join(path, target)
        if os.path.isfile(target_path):
            step(n)
            print(f'FILE: {target_path}')
        else:
            step(n)
            print(f'DIRECTORY: {target_path}')
            ShowAll(target_path, n+1)


path = input()
ShowAll(path, 0)


check = input()
print("Existing: ", os.access(check, os.F_OK))
print("Readable: ", os.access(check, os.R_OK))
print("Writability: ", os.access(check, os.W_OK))
print("Executability: ", os.access(check, os.X_OK))

