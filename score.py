import os



path = sorted(os.listdir())
print(path)
for i in path:
    path = os.path.join(i, "solution.py")
    print(path)
    if "math" in path:
        os.system("python3 " + path)
        print()
