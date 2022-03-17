import os
file = input()
s = os.path.dirname(__file__)+'/'+file
if os.path.exists(s):
    try:
        os.remove(os.path.dirname(__file__) + '/' + file)
    except:
        print("Can't delete")
else:
    print("Can't find")