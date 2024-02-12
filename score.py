import os

path = sorted(os.listdir())
for i in path:
    path = os.path.join(i, "solution.py")
    if "math" in path:
        os.system("python3 " + path)
