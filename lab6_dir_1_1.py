import os
path = os.getcwd()
for root, dirs, files in os.walk(path):
    for d in dirs:
        print(f'DiRectory: {root}/{d}')
    for f in files:
        print(f'File: {root}{dirs}{f}')
