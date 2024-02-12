import os

path = sorted(os.listdir())
cont = 1
for i in path:
    path = os.path.join(i, "solution.py")
    if "math" in path:
        print(cont)
        os.system("pylint " + path)
        cont+=1
