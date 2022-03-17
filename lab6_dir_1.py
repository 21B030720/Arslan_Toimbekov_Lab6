import os

def steps(n):
    print("<<|"*n, end = "")

def ShowAll(path, n):
    for target in os.listdir(path):
        target_path = os.path.join(path, target)
        if os.path.isfile(target_path):
            steps(n)
            print(f'PY: {target_path}')
        else:
            steps(n)
            print(f'FOLDER: {target_path}')
            ShowAll(target_path, n+1)

path = input("Print the path what you need to check")
ShowAll(path, 0)

